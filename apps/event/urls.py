from django.urls import path
from .views import EventListView, EventCreateView, EventUpdateView, EventDeleteView


app_name = 'event'
urlpatterns = (
    path('', EventListView.as_view(), name='list'),
    path('create/<int:pk>/', EventCreateView.as_view(), name='create'),
    path('update/<int:pk>/', EventUpdateView.as_view(), name='update'),
    path('delete/<int:pk>/', EventDeleteView.as_view(), name='delete'),
)