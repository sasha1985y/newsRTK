from django.contrib import admin
from django.db.models.functions import Length
from django.db.models import Count
from .models import *

class ArticleImageInline(admin.TabularInline):
    model = Image
    extra = 3
    readonly_fields = ('id','image_tag')
class ArticleAdmin(admin.ModelAdmin):
    list_display = ['title','author','date', 'symbols_count','image_tag']
    list_filter = ['title','author','date']
    # ordering = ['-date', 'title', 'author'] сортировка
    # list_display_links = ('date',) ссылки
    # list_editable = ['author'] редактировать поле автор или что-то ещё
    # readonly_fields = ['author','title'] нельзя редактировать
    list_per_page = 5
    inlines = [ArticleImageInline, ]

    @admin.display(description='Длина', ordering='_symbols')
    def symbols_count(self, article: Article):
        return f"Символы: {len(article.text)}"

    def get_queryset(self, request):
        queryset = super().get_queryset(request)
        queryset = queryset.annotate(_symbols=Length('text'))
        return queryset
@admin.register(Tag)#второй способ
class TagAdmin(admin.ModelAdmin):
    list_display = ['title','status','tag_count']
    list_filter = ['title','status']

    @admin.display(description='Использований:', ordering='tag_count')
    def tag_count(self, object):
        return object.tag_count

    def get_queryset(self, request):
        queryset = super().get_queryset(request)
        queryset = queryset.annotate(tag_count=Count('article'))
        return queryset

#admin.site.register(Tag,TagAdmin) первый способ зарегестрировать поля класса
admin.site.register(Article,ArticleAdmin)

@admin.register(Image)
class ImageAdmin(admin.ModelAdmin):
    list_display = ['title','article','image_tag']