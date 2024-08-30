# inventory/admin.py
from django.contrib import admin
from .models import Item, RecordItem, Record

class ItemAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'benefits')
    search_fields = ('name',)

class RecordItemAdmin(admin.ModelAdmin):
    list_display = ('item', 'quantity', 'record', 'amount')
    search_fields = ('item__name', 'record__client_name')
    readonly_fields = ('amount',)

class RecordAdmin(admin.ModelAdmin):
    list_display = ('client_name', 'total_amount', 'total_benefits')
    search_fields = ('client_name',)
    readonly_fields = ('total_amount', 'total_benefits')

admin.site.register(Item, ItemAdmin)
admin.site.register(RecordItem, RecordItemAdmin)
admin.site.register(Record, RecordAdmin)
