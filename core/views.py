from typing import Any
from django.shortcuts import render
from django.views.generic import TemplateView
from train.models import Station,Train_list
from django.core.exceptions import ObjectDoesNotExist

# Create your views here.
class HomeView(TemplateView):
    template_name='index.html'
    model = Station

    def get_context_data(self, **kwargs: Any):
        context = super().get_context_data(**kwargs)
        context['trains'] = Train_list.objects.all()

        station_slug = self.kwargs.get('station_slug')
        if station_slug:
            try:
                station = Station.objects.get(slug=station_slug)
                context['trains'] = Train_list.objects.filter(station=station)
            except ObjectDoesNotExist:
                pass
        context['station'] = Station.objects.all()
        return context