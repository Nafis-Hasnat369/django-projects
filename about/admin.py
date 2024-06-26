from django.contrib import admin
from about.models import Teacher

# Register your models here.


class TeacherAdmin(admin.ModelAdmin):
    list_display = ('id', 'teacher_id', 'teacher_name', 'teacher_email')


admin.site.register(Teacher, TeacherAdmin)
