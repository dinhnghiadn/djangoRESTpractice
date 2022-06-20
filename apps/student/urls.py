from django.urls import path, include
from rest_framework.routers import DefaultRouter
from apps.student.views import StudentViewSet

router = DefaultRouter()
router.register("", StudentViewSet, basename="student")

app_name = 'myStudent'
urlpatterns = [
    path('', include(router.urls)),
]
