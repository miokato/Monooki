from django.shortcuts import render
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from .models import Event, Ticket
from .forms import EventForm


class EventListView(ListView):
    model = Event
    context_object_name = 'events'
    template_name = 'event/event_list.html'


class EventCreateView(CreateView):
    model = Event
    form_class = EventForm
    context_object_name = 'events'
    template_name = 'event/event_form.html'
    success_url = '/event'

    def form_valid(self, form):
        event = form.save(commit=False)
        event.user = self.request.user
        event.save()

        return super().form_valid(form)


class EventUpdateView(UpdateView):
    model = Event
    context_object_name = 'events'
    template_name = 'event/event_form.html'


class EventDeleteView(DeleteView):
    model = Event
    context_object_name = 'events'



