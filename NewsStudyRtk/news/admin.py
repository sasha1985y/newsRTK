from django.contrib import admin
from django.db.models.functions import Length
from django.db.models import Count
from .models import *

class ArticleFilter(admin.SimpleListFilter):
    title = 'По длине новости'
    parameter_name = 'text'

    def lookups(self, request, model_admin):
        return [('S',("Короткие, <100 зн.")),
                ('M',("Средние, 100-500 зн.")),
                ('L',("Длинные, >500 зн.")),]

    def queryset(self, request, queryset):
        if self.value() == 'S':
            return queryset.annotate(text_len=Length('text')).filter(text_len__lt=100)
        elif self.value() == 'M':
            return queryset.annotate(text_len=Length('text')).filter(text_len__lt=500,
                                                                     text_len__gte=100)
        elif self.value() == 'L':
            return queryset.annotate(text_len=Length('text')).filter(text_len__gt=500)

class ArticleImageInline(admin.TabularInline):
    model = Image
    extra = 3
    readonly_fields = ('id','image_tag')
class ArticleAdmin(admin.ModelAdmin):
    list_display = ['title','author','date', 'symbols_count','image_tag']
    list_filter = ['date', ArticleFilter]
    # ordering = ['-date', 'title', 'author'] сортировка
    # list_display_links = ('date',) ссылки
    # list_editable = ['author'] редактировать поле автор или что-то ещё
    # readonly_fields = ['author','title'] нельзя редактировать
    list_per_page = 5
    inlines = [ArticleImageInline, ]
    # search_fields = ['title__startswith', 'tags__title']
    filter_horizontal = ['tags']

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

@admin.register(ViewCount)
class ViewCountAdmin(admin.ModelAdmin):
    list_display = ['article','ip_address','view_date']