from rest_framework import serializers

from apps.classes.models import Class


class ClassSerializer(serializers.ModelSerializer):
    class Meta:
        model = Class
        fields = ['id', 'name', 'date_create', 'subject']
