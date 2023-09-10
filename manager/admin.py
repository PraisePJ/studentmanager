from django.contrib import admin
from .models import Student, Staff, Result, Project

# Register your models here.
admin.site.register(Student)
admin.site.register(Staff)
admin.site.register(Result)
admin.site.register(Project)