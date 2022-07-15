from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView, TokenVerifyView
from rest_framework import routers
from django.urls import include, path
from .views import *

router = routers.DefaultRouter()
router.register('user', UserView)
router.register('profile', ProfileView)

urlpatterns = [
    path('', include(router.urls)),
    path('login/', TokenObtainPairView.as_view(), name='login'),
    path('verify/', TokenVerifyView.as_view(), name='verify'),
    path('refresh/', TokenRefreshView.as_view(), name='refresh'),
]