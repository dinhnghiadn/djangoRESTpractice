from django.db import models


class Subject(models.Model):
    TERM_CHOICES = (
        ('1', 'First'),
        ('2', 'Second'),
    )

    name = models.CharField(max_length=50)
    term = models.CharField(max_length=1, choices=TERM_CHOICES)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "My Subjects"
        db_table = 'subject'
