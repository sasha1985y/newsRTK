from django.contrib import admin
from .models import Demo
# Register your models here.


class DemoAdmin(admin.ModelAdmin):
    list_display = ['title','image','image_tag']

admin.site.register(Demo,DemoAdmin)