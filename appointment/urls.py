from django.urls import path, include
from rest_framework import routers
from . import views

router = routers.DefaultRouter()

##Antena
router.register('',views.AppointmentViewSet)

urlpatterns = [
    path('',include(router.urls)),
    
]

