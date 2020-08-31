from django import forms
from django.contrib.gis.db import models
from rest_framework_gis.serializers import GeoFeatureModelSerializer


class Location(forms.Form):
    Name = forms.IntegerField()
    Geo = models.TextField()


class Entry(models.Model):
    City = models.CharField(max_length=255)
    latitude = models.PointField()
    longitude = models.PointField()

    def __str__(self):
        return self.City


class AdSerializer(GeoFeatureModelSerializer):
    class Meta:
        geo_field = 'City'
        fields = ('id',)
