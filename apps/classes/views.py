from django.http import JsonResponse
from rest_framework import status, viewsets
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView, get_object_or_404
from rest_framework.permissions import IsAuthenticated

from apps.classes.models import Class
from apps.classes.serializer import ClassSerializer


class ClassViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    serializer_class = ClassSerializer

    def get_queryset(self):
        classes = Class.objects.all().order_by('name')
        return classes
