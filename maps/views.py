# import City as City
from django.shortcuts import render
from django.views import generic
from rest_framework.viewsets import ReadOnlyModelViewSet
from rest_framework_gis.filters import InBBoxFilter
from django.db import models as Entry

from maps.models import Entry, AdSerializer


class index(generic.TemplateView):
    template_name = 'html.html'


class AdViewSet(ReadOnlyModelViewSet):
    bbox_filter_field = 'City'
    filter_backends = (InBBoxFilter,)
    serializer_class = AdSerializer


def passing(request):
    lat = Entry.latitude
    long = Entry.longitude
    city = Entry.City
    lat_long = list(zip(lat, long))
    return render(request, 'html.html', {'titles': city}, {'lat_long': lat_long})


def please_work(request):
    data = Entry.objects.all()
    context = {
        'worldCity': data,
    }
    return render(request, 'html.html', context)
