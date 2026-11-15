from rest_framework.routers import DefaultRouter
from django.urls import path, include
from .views import ServiceViewSet

router = DefaultRouter() # This is router

# This is router antena
router.register('', ServiceViewSet, ) ## ek ekta viewset er jonno ekta URL pattern create

urlpatterns = [
    path("", include(router.urls)), ## router.urls er moddhome sob URL pattern gula ke include kora hoyeche
]