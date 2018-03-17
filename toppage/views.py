from django.shortcuts import render
from django.views.generic import ListView
from item.models import Item


class ItemListView(ListView):
    template_name = 'toppage/home.html'
    model = Item
    context_object_name = 'items'




