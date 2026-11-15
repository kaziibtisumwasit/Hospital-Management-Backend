from django.shortcuts import render
from rest_framework import viewsets
from .models import Service
from .serializers import ServiceSerializer
# Create your views here.


class ServiceViewSet(viewsets.ModelViewSet):
    queryset = Service.objects.all() ## Get all object or fields from Service model
    serializer_class = ServiceSerializer ## Serializer class er moddhome model er sob field gula ke
    ## queryset & serializer_class is built-in attributes of ModelViewSet