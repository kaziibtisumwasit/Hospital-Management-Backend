from django.shortcuts import render
from rest_framework import viewsets
from . import models
from . import serializers


# Create your views here.


## JSON Conversion of the Appointment model.
class AppointmentViewSet(viewsets.ModelViewSet):
    queryset = models.Appointment.objects.all()
    serializer_class = serializers.AppointmentSerializer 
    
    ## Customizing the queryset to filter appointments based on the doctor or patient. This is done by overriding the get_queryset method of the viewset. The get_queryset method is called when a request is made to the viewset, and it returns the queryset that will be used to retrieve the data for the response. In this case, we are checking if the request has a 'doctor' or 'patient' parameter in the query string, and if so, we filter the queryset accordingly.
    def get_queryset(self):
        queryset = super().get_queryset() ## queryset ke inherite korlam
        # doctor_id = self.request.query_params.get('doctor')
        patient_id = self.request.query_params.get('patient_id')
        ## params means Parameters
        # if doctor_id:
        #     queryset = queryset.filter(doctor__id=doctor_id)
        if patient_id:
            queryset = queryset.filter(patient_id=int(patient_id))
            # print("Patient ID:", patient_id)
        return queryset