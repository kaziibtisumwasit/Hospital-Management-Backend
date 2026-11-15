from django.shortcuts import render

from rest_framework import viewsets
from . import models
from .serializers import DoctorSerializer , SpecializationSerializer , AvailableTimeSerializer , DesignationSeralizer , ReviewSerializer        


# Create your views here.


class DoctorViewSet(viewsets.ModelViewSet):
    queryset = models.Doctor.objects.all()
    serializer_class = DoctorSerializer
    


class SpecializationViewSet(viewsets.ModelViewSet):
    queryset = models.Specialization.objects.all()
    serializer_class = SpecializationSerializer
    
class AvailableTimeViewSet(viewsets.ModelViewSet):
    queryset = models.AvailableTime.objects.all()
    serializer_class = AvailableTimeSerializer
    
    
class DesignationViewSet(viewsets.ModelViewSet):
    queryset = models.Designation.objects.all()
    serializer_class = DesignationSeralizer
    


class ReviewViewSet(viewsets.ModelViewSet):
    queryset = models.Review.objects.all()
    serializer_class = ReviewSerializer