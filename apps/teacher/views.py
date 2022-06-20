from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from apps.teacher.models import Teacher
from apps.teacher.serializer import TeacherSerializer


class TeacherViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    serializer_class = TeacherSerializer

    def get_queryset(self):
        teacher = Teacher.objects.all()
        return teacher
