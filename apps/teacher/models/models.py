from django.db import models

from apps.classes.models.models import Class
from apps.subject.models.models import Subject


class Teacher(models.Model):
    GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
    )

    name = models.CharField(max_length=50)
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    classes = models.ForeignKey(Class, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "My Teachers"
        db_table = 'teacher'
