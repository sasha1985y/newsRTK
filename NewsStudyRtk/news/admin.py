from django import forms
from django.contrib import admin
from django.db.models.functions import Length
from django.db.models import Count
from .models import *
from ckeditor_uploader.widgets import CKEditorUploadingWidget

class ArticleAdminForm(forms.ModelForm):
    text = forms.CharField(label="Текст новости", widget=CKEditorUploadingWidget())
    # anouncement = forms.CharField(label="Аннотация", widget=CKEditorUploadingWidget())
    class Meta:
        model = Article
        fields = '__all__'

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
    extra = 1
    readonly_fields = ('id','image_tag')

class ArticleAdmin(admin.ModelAdmin):
    ordering = ['-date','categories','author','title']
    list_display = ['id','date','status','categories','author','image_tag','title','source','symbols_count']
    list_filter = [ArticleFilter,'title','author','date','categories','source']
    list_display_links = ['date']
    search_fields = ['title__startswith','tags__title']
    filter_horizontal = ['tags']
    form = ArticleAdminForm
    # list_editable = ['status'] #Возможность редактирования содержимого из списка
    # readonly_fields = ['author'] #Закрытие редактирования
    # prepopulated_fields = {"author":("title")} #Предзаполненные поля
    # list_per_page = 5 # Количество записей на странице (пагинация)
    inlines = [ArticleImageInline,]
    actions = ['set_true','set_false']

    @admin.display(description='Количество символов',ordering='_simbols')
    def symbols_count(self, article:Article):
        return f"{len(article.text)}"

    def get_queryset(self, request):
        queryset = super().get_queryset(request)
        queryset = queryset.annotate(_simbols=Length('text'))
        return queryset

    @admin.action(description='Активировать выбранные новости')
    def set_true(self, request, queryset):
        amount = queryset.update(status=True)
        self.message_user(request, f'Активировано {amount} новостей')

    @admin.action(description='Деактивировать выбранные новости')
    def set_false(self, request, queryset):
        amount = queryset.update(status=False)
        self.message_user(request, f'Деактивировано {amount} новостей')


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

class SubscriberAdmin(admin.ModelAdmin):
    list_display = ['last_name', 'first_name', 'email']
    list_filter = ['last_name', 'first_name', 'email']


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