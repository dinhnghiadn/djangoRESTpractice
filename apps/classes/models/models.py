from django.db import models

from apps.subject.models.models import Subject


class Class(models.Model):
    name = models.CharField(max_length=5)
    date_create = models.DateField(max_length=15)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "My Classes"
        db_table = 'classes'
        ordering = ['name']
