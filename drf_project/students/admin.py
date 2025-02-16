from django.contrib import admin
from .models import Student

# Register your models here.


@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('student_id', 'name', 'branch')
    list_filter = ('branch',)
