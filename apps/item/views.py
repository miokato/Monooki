from django.shortcuts import get_object_or_404, render
from .models import Item


def detail(request, slug):
    item = get_object_or_404(Item, slug=slug)

    return render(request, 'items/detail.html', {'item': item})
