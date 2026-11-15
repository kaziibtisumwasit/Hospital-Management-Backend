## Create JSON Router
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ContactUsViewSet


## This is router
router = DefaultRouter() ## This is router object. This router object will automatically generate the URL patterns for the viewset.


# This is router antena
router.register('', ContactUsViewSet,) ## ek ekta viewset er jonno ekta URL pattern create



urlpatterns = [
    ## ei router er jotoghula views handle korbe sob empty path er moddhome include kora hoyeche
    path("", include(router.urls)), ## router.urls er moddhome sob URL pattern gula ke include kora hoyeche
]
