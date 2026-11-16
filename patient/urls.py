from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import PatientViewSet , PatientRegistrationView

## This is router
router = DefaultRouter()

router.register('list',PatientViewSet,)


urlpatterns = [
    path('',include(router.urls)),
    path('register/',PatientRegistrationView.as_view(),name='patient-register'),
]
