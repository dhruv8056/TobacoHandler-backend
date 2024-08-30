# inventory/forms.py
from django import forms
from .models import Item, Record,RecordItem

class ItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = ['name', 'price', 'benefits']

class RecordForm(forms.ModelForm):
    class Meta:
        model = Record
        fields = ['client_name']
        widgets = {
            'items': forms.SelectMultiple(attrs={'class': 'select2-multiple'}),
        }
class RecordItemForm(forms.ModelForm):
    class Meta:
        model = RecordItem
        fields = ['item', 'quantity']