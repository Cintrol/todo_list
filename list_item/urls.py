from django.contrib import admin
from django.urls import path, include
from list_item.views import list_item_view, edit_list_view, create_list_view, delete_list_view

app_name = 'list_item'

urlpatterns = [
    path('<int:pk>', list_item_view, name='list_item'),
    path('<int:pk>/', list_item_view, name='list_item'),
    path('create/<int:pk>', create_list_view, name='create'),
    path('edit/<int:pk>', edit_list_view, name='list_edit'),
    path('delete/<int:pk>', delete_list_view, name='delete_edit'),
]