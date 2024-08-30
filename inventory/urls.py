# urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('add-item/', views.add_item, name='add_item'),
    path('list-items/', views.list_items, name='list_items'),
    path('create-record/', views.create_record, name='create_record'),
    path('list-records/', views.list_records, name='list_records'),
    path('search-items/', views.search_items, name='search_items'),
]
