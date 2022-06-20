from django.contrib import admin
from django.db import models
from apps.classes.models.models import Class


class Student(models.Model):
    GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
    )

    name = models.CharField(max_length=50)
    date_of_birth = models.DateField(max_length=100)
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    email = models.CharField(max_length=50)
    address = models.CharField(max_length=50)
    classes = models.ManyToManyField(Class)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "My Students"
        db_table = 'student'

    @admin.display(
        description='Class parcitipated',
    )
    def get_classes(self):
        return ", ".join([s.name for s in self.classes.all()])
