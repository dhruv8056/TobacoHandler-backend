# serializers.py
from rest_framework import serializers
from .models import Item, Record, RecordItem

class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = '__all__'

class RecordItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = RecordItem
        fields = '__all__'

class RecordSerializer(serializers.ModelSerializer):
    record_items = RecordItemSerializer(many=True, read_only=True)

    class Meta:
        model = Record
        fields = '__all__'
