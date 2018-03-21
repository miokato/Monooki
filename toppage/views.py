from django.shortcuts import render
from django.views.generic import ListView
from item.models import Item
from news.models import News


class ItemListView(ListView):
    template_name = 'toppage/home.html'
    model = Item
    context_object_name = 'items'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['news_list'] = News.objects.all().order_by('-pub_date')[:5]

        return context






