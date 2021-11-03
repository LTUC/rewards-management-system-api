from django.contrib import admin
from .models import Rewad, Course, Student, AssignRole
# Register your models here.

admin.site.register(Course)
admin.site.register(AssignRole)
admin.site.register(Rewad)
admin.site.register(Student)