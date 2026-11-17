from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import PatientViewSet , PatientRegistrationView , activate_account , userLoginApiView , userLogoutView

## This is router
router = DefaultRouter()

router.register('list',PatientViewSet,)


urlpatterns = [
    path('',include(router.urls)),
    path('register/',PatientRegistrationView.as_view(),name='patient-register'),
    path('active/<uid64>/<token>/',activate_account,name='patient-activate'),
    path('login/',userLoginApiView.as_view(),name='patient-login'),
    path('logout/', userLogoutView.as_view(), name='patient-logout'),
]
