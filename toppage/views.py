from django.shortcuts import render
from django.views.generic import ListView
from item.models import Item


class ItemListView(ListView):
    template_name = 'toppage/item-list.html'
    model = Item




