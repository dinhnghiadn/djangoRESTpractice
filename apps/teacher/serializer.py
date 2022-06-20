from rest_framework import serializers

from apps.teacher.models import Teacher


class TeacherSerializer(serializers.ModelSerializer):
    # teacher_id = serializers.IntegerField(read_only=True, required=True)
    # name = serializers.CharField(required=True, allow_blank=False, max_length=50)
    # subject_taught = serializers.IntegerField(required=True)

    class Meta:
        model = Teacher
        fields = "__all__"
