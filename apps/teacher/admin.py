from django.contrib import admin

from apps.subject.models import Subject
from apps.teacher.models import Teacher


class TeacherAdmin(admin.ModelAdmin):
    list_display = ('name', 'gender', 'classes', 'subject',)
    search_fields = ['name']


admin.site.register(Teacher, TeacherAdmin)
