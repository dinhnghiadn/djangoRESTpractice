from rest_framework import serializers

from apps.classes.models import Class
from apps.classes.serializer import ClassSerializer
from apps.student.models import Student


class StudentSerializer(serializers.ModelSerializer):
    classes = ClassSerializer(many=True, read_only=False)

    class Meta:
        model = Student
        fields = ['id', 'name', 'date_of_birth', 'gender', 'email', 'address', 'classes']
        depth = 1

    def create(self, validated_data):
        class_data = validated_data.pop('classes')
        student = Student.objects.create(**validated_data)
        for cl in class_data:
            cl_object = Class.objects.get(name__iexact=cl["name"])
            student.classes.add(cl_object)
        return student

    def update(self, instance, validated_data):
        class_data = validated_data.pop('classes')
        instance = super(StudentSerializer, self).update(instance, validated_data)
        instance.classes.clear()
        for cl in class_data:
            cl_qs = Class.objects.filter(name__iexact=cl['name'])
            if cl_qs.exists():
                cl_object = cl_qs.first()
            else:
                cl_object = Class.objects.create(**cl)
            instance.classes.add(cl_object)

        return instance

