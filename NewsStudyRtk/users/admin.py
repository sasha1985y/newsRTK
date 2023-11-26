from django.contrib import admin
from .models import *
class AccountAdmin(admin.ModelAdmin):
    list_display = ['user','gender']
    list_filter = ['user','gender']

admin.site.register(Account,AccountAdmin)
