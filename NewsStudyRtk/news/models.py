from django.db import models
import datetime
from django.contrib.auth.models import User
from django.utils.safestring import mark_safe
from users.models import Account

class Tag(models.Model):
    title = models.CharField(max_length=80)
    status = models.BooleanField(default=True)
    def __str__(self):
        return self.title
    class Meta:
        ordering = ['title','status']
        verbose_name= 'Тэг'
        verbose_name_plural='Тэги'


class PublishedToday(models.Manager):
    def get_queryset(self):
        return super(PublishedToday,self).get_queryset().filter(date__gte=datetime.date.today())

class Article(models.Model):
    #title = models.CharField(max_length=30)

    categories = (('E','Economics'),
                  ('S','Science'),
                  ('IT','IT'))
    #поля                           #models.CASCADE SET_DEFAULT
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    account = models.ForeignKey(Account, on_delete=models.SET_NULL, null=True)
    title = models.CharField('Название',max_length=50,default='')
    anouncement = models.TextField('Аннотация',max_length=250)
    text = models.TextField('Текст новости')
    date = models.DateTimeField('Дата публикации',auto_now=True)
    category = models.CharField(choices=categories, max_length=20,verbose_name='Категории')
    #image = models.ImageField(blank=True, upload_to='images/')
    tags = models.ManyToManyField(to=Tag, blank=True)
    #slug = models.SlugField()
    objects = models.Manager()
    published = PublishedToday()

    #методы моделей
    def __str__(self):
        return f'{self.title} от: {str(self.date)[:16]}'

    def get_absolute_url(self):
        return f'/news/show/{self.id}'

    def tag_list(self):
        s = ''
        for t in self.tags.all():
            s += t.title + ' '
        return s

    def image_tag(self):
        image = Image.objects.filter(article=self)
        if image:
            return mark_safe(f'<img src="{image[0].image.url}" height="50px" width="auto" />')
        else:
            return '(no image)'

    def get_absolute_url_public(self):
        return f'/news/show/public/{self.author_id}'
    #метаданные модели

    def get_views(self):
        return self.views.count()

    class Meta:
        ordering = ['title','date']
        verbose_name= 'Новость'
        verbose_name_plural='Новости'


class Image(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    title = models.CharField(max_length=50, blank=True)
    image = models.ImageField(upload_to='article_images/')

    def __str__(self):
        return self.title

    def image_tag(self):
        if self.image is not None:
            return mark_safe(f'<img src="{self.image.url}" height="50px" width="auto" />')
        else:
            return '(no image)'

class ViewCount(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE,
                                related_name='views')
    ip_address = models.GenericIPAddressField()
    view_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('-view_date',)
        indexes = [models.Index(fields=['-view_date'])]

    def __str__(self):
        return self.article.title