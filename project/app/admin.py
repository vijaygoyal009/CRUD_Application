from django.contrib import admin
from .models import Student
# Register your models here.

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('id','name','email','password')




# This is the first way to add our models in admin file
#admin.site.register(Student)
