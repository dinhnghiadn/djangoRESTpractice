from django.contrib import admin

from apps.student.models import Student


class StudentAdmin(admin.ModelAdmin):
    list_display = ('name', 'gender', 'date_of_birth', 'get_classes')
    list_filter = ['date_of_birth']
    search_fields = ['name']


admin.site.register(Student, StudentAdmin)
