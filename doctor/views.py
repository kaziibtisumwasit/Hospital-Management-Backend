from django.shortcuts import render

from rest_framework import viewsets
from . import models
from .serializers import DoctorSerializer , SpecializationSerializer , AvailableTimeSerializer , DesignationSeralizer , ReviewSerializer        
from rest_framework.permissions import IsAuthenticated

# Create your views here.


class DoctorViewSet(viewsets.ModelViewSet):
    queryset = models.Doctor.objects.all()
    serializer_class = DoctorSerializer
    


class SpecializationViewSet(viewsets.ModelViewSet):
    queryset = models.Specialization.objects.all()
    serializer_class = SpecializationSerializer
    
class AvailableTimeViewSet(viewsets.ModelViewSet):
    # SECURE REST Framework API with IsAuthenticated permission class. 
    permission_classes = [IsAuthenticated]  # Only authenticated users can access this viewset  . Setting permission_classes to IsAuthenticated ensures that only users who are logged in can access the AvailableTimeViewSet. If a user is not authenticated, they will receive a 403 Forbidden response when trying to access this viewset.
    queryset = models.AvailableTime.objects.all()
    serializer_class = AvailableTimeSerializer
    
    
class DesignationViewSet(viewsets.ModelViewSet):
    queryset = models.Designation.objects.all()
    serializer_class = DesignationSeralizer
    


class ReviewViewSet(viewsets.ModelViewSet):
    queryset = models.Review.objects.all()
    serializer_class = ReviewSerializer