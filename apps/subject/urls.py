from django.urls import path, include
from rest_framework.routers import DefaultRouter
from apps.subject.views import SubjectViewSet

router = DefaultRouter()
router.register("", SubjectViewSet, basename="subject")

app_name = 'mySubject'
urlpatterns = [
    path('', include(router.urls)),
]