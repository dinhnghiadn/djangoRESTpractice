from django.contrib import admin

from apps.classes.models import Class


class ClassAdmin(admin.ModelAdmin):
    list_display = ('name', 'date_create', 'subject')
    list_filter = ['date_create']
    search_fields = ['subject__name']


admin.site.register(Class, ClassAdmin)
