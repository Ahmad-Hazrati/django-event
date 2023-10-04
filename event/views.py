from django.shortcuts import render
from django.views import generic
from .models import Event, Category


class EventList(generic.ListView):
    model = Event
    queryset = Event.objects.filter(status=1).order_by('-created_on')
    template_name = 'home.html'
    paginate_by = 6
