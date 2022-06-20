from rest_framework import serializers

from apps.subject.models import Subject


class SubjectSerializer(serializers.ModelSerializer):
    # subject_id = serializers.IntegerField(read_only=True, required=True)
    # name = serializers.CharField(required=True, allow_blank=False, max_length=100)

    class Meta:
        model = Subject
        fields ="__all__"