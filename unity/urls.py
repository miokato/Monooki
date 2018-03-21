from django.urls import path
from django.views.generic import TemplateView

app_name = 'game'
urlpatterns = (
    path('tutorial/', TemplateView.as_view(template_name='game/tutorial.html'), name='first'),
)
