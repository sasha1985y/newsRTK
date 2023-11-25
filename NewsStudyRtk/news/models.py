from django.db import models

from django.contrib.auth.models import User
from django.utils.safestring import mark_safe

class Article(models.Model):
    #title = models.CharField(max_length=30)

    categories = (('E','Economics'),
                  ('S','Science'),
                  ('IT','IT'))
    #поля                           #models.CASCADE SET_DEFAULT
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    title = models.CharField('Название',max_length=50,default='')
    anouncement = models.TextField('Аннотация',max_length=250)
    text = models.TextField('Текст новости')
    date = models.DateTimeField('Дата публикации',auto_now=False)
    category = models.CharField(choices=categories, max_length=20,verbose_name='Категории')
    image = models.ImageField(blank=True, upload_to='images/')

    #методы моделей
    def __str__(self):
        return f'{self.title} от: {str(self.date)[:16]}'

    def get_absolute_url(self):
        return f'/news/show/{self.id}'
    #метаданные модели

    class Meta:
        ordering = ['title','date']
        verbose_name= 'Новость'
        verbose_name_plural='Новости'

    def image_tag(self):
        if self.image is not None:
            return mark_safe('<img src="{}" height="50"/>'.format(self.image.url))