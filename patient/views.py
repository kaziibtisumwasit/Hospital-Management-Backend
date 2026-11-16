from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.views import APIView
from .models import Patient
from .serializers import PatientSerializer , PatientRegistrationSerializer 


class PatientViewSet(viewsets.ModelViewSet):
    queryset = Patient.objects.all() ## For Get Req
    serializer_class = PatientSerializer
    

## ApiView can use any where like classbased View.
class PatientRegistrationView(APIView):
    serializer_class = PatientRegistrationSerializer
    
    # def post(self, request):
    #     self.serializer_class = PatientRegistrationSerializer(data=request.data)

