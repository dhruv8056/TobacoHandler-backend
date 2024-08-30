# views.py
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Item, Record, RecordItem
from .serializers import ItemSerializer, RecordSerializer, RecordItemSerializer

@api_view(['POST'])
def add_item(request):
    if request.method == 'POST':
        serializer = ItemSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def list_items(request):
    items = Item.objects.all()
    serializer = ItemSerializer(items, many=True)
    return Response(serializer.data)

@api_view(['POST'])
def create_record(request):
    if request.method == 'POST':
        serializer = RecordSerializer(data=request.data)
        if serializer.is_valid():
            record = serializer.save()
            items = request.data.get('items')
            quantities = request.data.get('quantities')
            for item_id, quantity in zip(items, quantities):
                RecordItem.objects.create(record=record, item_id=item_id, quantity=int(quantity))
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def list_records(request):
    records = Record.objects.all()
    record_details = []

    total_amount = 0
    total_benefits = 0
    for record in records:
        record_total_amount = record.total_amount()
        record_total_benefits = record.total_benefits()
        total_amount += record_total_amount
        total_benefits += record_total_benefits

        record_details.append({
            'client_name': record.client_name,
            'items': RecordItemSerializer(record.record_items.all(), many=True).data,
            'total_amount': record_total_amount,
            'total_benefits': record_total_benefits,
        })

    return Response({
        'record_details': record_details,
        'total_amount': total_amount,
        'total_benefits': total_benefits
    })

@api_view(['GET'])
def search_items(request):
    if 'term' in request.GET:
        qs = Item.objects.filter(name__icontains=request.GET.get('term'))
        print('qs: 11111111111111111111111   ', str(qs))
        items = list(qs.values('id', 'name'))
        return Response(items)
    return Response([], status=status.HTTP_200_OK)
