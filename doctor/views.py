from django.shortcuts import render

from rest_framework import viewsets
from . import models
from .serializers import DoctorSerializer , SpecializationSerializer , AvailableTimeSerializer , DesignationSeralizer , ReviewSerializer        
from rest_framework.permissions import IsAuthenticated , BasePermission ,IsAuthenticatedOrReadOnly 
from rest_framework import pagination, filters
# Create your views here.





class DoctorPagination(pagination.PageNumberPagination):
    page_size = 1  # Number of items per page
    page_size_query_param = 'page_size'  # Allow clients to set the page size via query parameter
    max_page_size = 100  # Maximum page size allowed
    
    
    
class DoctorViewSet(viewsets.ModelViewSet):
    queryset = models.Doctor.objects.all()
    serializer_class = DoctorSerializer
    filter_backends = [filters.SearchFilter]  # Enable search functionality
    pagination_class = DoctorPagination 
    search_fields = ['user__first_name', 'user__last_name', 'specialization__name']  # Specify the fields to search on
    


class SpecializationViewSet(viewsets.ModelViewSet):
    queryset = models.Specialization.objects.all()
    serializer_class = SpecializationSerializer
    


class AvailableTimeForSpecificDoctor(filters.BaseFilterBackend):
    def filter_queryset(self, request, queryset, view):
        doctor_id = request.query_params.get('doctor_id')
        if doctor_id:
            return queryset.filter(doctor = doctor_id)
        return queryset

class AvailableTimeViewSet(viewsets.ModelViewSet):
    # SECURE REST Framework API with IsAuthenticated permission class. 
    permission_classes = [IsAuthenticated]  # Only authenticated users can access this viewset  . Setting permission_classes to IsAuthenticated ensures that only users who are logged in can access the AvailableTimeViewSet. If a user is not authenticated, they will receive a 403 Forbidden response when trying to access this viewset.
    queryset = models.AvailableTime.objects.all()
    serializer_class = AvailableTimeSerializer
    filter_backends = [AvailableTimeForSpecificDoctor]  # Apply the custom filter backend to filter available times based on doctor_id query parameter
    
class DesignationViewSet(viewsets.ModelViewSet):
    queryset = models.Designation.objects.all()
    serializer_class = DesignationSeralizer
    


class ReviewViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticatedOrReadOnly]  # Only authenticated users can create reviews, but anyone can read them   
    queryset = models.Review.objects.all()
    serializer_class = ReviewSerializer
    
    
## For Pagination,
