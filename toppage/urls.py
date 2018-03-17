from django.urls import path
from .views import ItemListView


app_name = 'top'
urlpatterns = [
    path('', ItemListView.as_view(), name='item-list'),
]