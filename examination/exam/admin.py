from django.contrib import admin
from .models import addQuestion,addSubject,Result 
# Register your models here.
admin.site.register([addQuestion,addSubject,Result])