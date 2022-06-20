from django.urls import path, include
from rest_framework.routers import DefaultRouter
from apps.subject.views import SubjectViewSet
from apps.teacher.views import TeacherViewSet

router = DefaultRouter()
router.register("", TeacherViewSet, basename="teacher")

app_name = 'myTeacher'
urlpatterns = [
    path('', include(router.urls)),
]