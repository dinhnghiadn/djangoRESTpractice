from django.urls import path, include
from rest_framework.routers import DefaultRouter

from apps.classes.views import ClassViewSet

router = DefaultRouter()
router.register("", ClassViewSet, basename="classes")

app_name = 'myClass'
urlpatterns = [
    path('', include(router.urls)),
]
