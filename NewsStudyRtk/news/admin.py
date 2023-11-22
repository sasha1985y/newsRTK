from django.contrib import admin


from .models import *

class ArticleAdmin(admin.ModelAdmin):
    list_display = ['title','author','date']
    list_filter = ['title','author','date']

admin.site.register(Article,ArticleAdmin)