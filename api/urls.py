from django.urls import include, path
from rest_framework import routers
from .views import *

router = routers.DefaultRouter()
router.register('post', PostView)
router.register('comment', CommentView)

urlpatterns = [
    path('', include(router.urls)),
]