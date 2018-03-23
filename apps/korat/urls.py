from django.urls import path
from django.views.generic import TemplateView

app_name = 'korat'
urlpatterns = (
    path('', TemplateView.as_view(template_name='korat/content.html'), name='content'),
)
