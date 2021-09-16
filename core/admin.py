from django.contrib import admin
from .models import Student, School

@admin.register(School)
class SchoolAdmin(admin.ModelAdmin):
	list_display = ['school', 'school_name']

admin.site.register(Student)