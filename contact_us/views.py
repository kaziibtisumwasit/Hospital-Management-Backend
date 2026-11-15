from django.shortcuts import render
from rest_framework import viewsets

from .models import ContactUs
from .serializers import ContactUsSerializer

# Create your views here.


class ContactUsViewSet(viewsets.ModelViewSet):
    queryset = ContactUs.objects.all() ## Get all object or fields from ContactUs model
    serializer_class = ContactUsSerializer ## Serializer class er moddhome model er sob field gula ke