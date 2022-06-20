from django.http import JsonResponse
from rest_framework import status, viewsets
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView, get_object_or_404
from rest_framework.permissions import IsAuthenticated

from apps.subject.models import Subject
from apps.subject.serializer import SubjectSerializer


class SubjectViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    serializer_class = SubjectSerializer

    def get_queryset(self):
        subject = Subject.objects.all()
        return subject
