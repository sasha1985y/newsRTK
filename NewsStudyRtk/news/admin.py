from django.contrib import admin


from .models import *

class ArticleAdmin(admin.ModelAdmin):
    list_display = ['title','author','date']
    list_filter = ['title','author','date']
    # ordering = ['-date', 'title', 'author'] сортировка
    # list_display_links = ('date',) ссылки
    # list_editable = ['author'] редактировать поле автор или что-то ещё
    # readonly_fields = ['author','title'] нельзя редактировать
@admin.register(Tag)#второй способ
class TagAdmin(admin.ModelAdmin):
    list_display = ['title','status']
    list_filter = ['title','status']

#admin.site.register(Tag,TagAdmin) первый способ зарегестрировать поля класса
admin.site.register(Article,ArticleAdmin)