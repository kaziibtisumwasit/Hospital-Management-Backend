from django.urls import path , include 
from rest_framework.routers import DefaultRouter
from .views import DoctorViewSet , SpecializationViewSet , AvailableTimeViewSet , DesignationViewSet , ReviewViewSet    


## This is router
router = DefaultRouter()


router.register('doctorlist',DoctorViewSet,)
router.register('specialization',SpecializationViewSet,)
router.register('available-time',AvailableTimeViewSet,)
router.register('designation',DesignationViewSet,)
router.register('review',ReviewViewSet,)


urlpatterns = [
    path('',include(router.urls))
]
