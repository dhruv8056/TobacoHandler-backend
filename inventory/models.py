# inventory/models.py
from django.db import models

class Item(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    benefits = models.IntegerField()

    def __str__(self):
        return self.name

class RecordItem(models.Model):
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()
    record = models.ForeignKey('Record', related_name='record_items', on_delete=models.CASCADE)

    @property
    def amount(self):
        return self.item.price * self.quantity


class Record(models.Model):
    client_name = models.CharField(max_length=100)
    date_created = models.DateTimeField(auto_now_add=True,null=True,blank=True)  # Automatically set to current date and time when created

    def total_amount(self):
        return sum(record_item.amount for record_item in self.record_items.all())

    def total_benefits(self):
        return sum(record_item.item.benefits * record_item.quantity for record_item in self.record_items.all())

    def __str__(self):
        return self.client_name