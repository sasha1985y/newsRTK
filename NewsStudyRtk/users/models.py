from ckeditor.fields import RichTextField
from .validators import russian_email
from django.core.validators import MinLengthValidator
from django.db import models
from django.contrib.auth.models import User
from news.models import Article
class Account(models.Model):
    gender_choices= (('M','Male'),
                     ('F','Female'),
                     ('N/A','Not answered'))
    user = models.OneToOneField(User,on_delete=models.CASCADE,
                                primary_key=True)
    nickname = models.CharField(max_length=100,blank=True)
    birthdate = models.DateField(null=True)
    gender = models.CharField(choices=gender_choices,max_length=20)
    account_image = models.ImageField(default='default.jpg',
                                      upload_to='account_images')

    address = models.CharField(max_length=100,blank=True)
    job = models.CharField(max_length=100,blank=True)
    whatsapp = models.CharField(max_length=100, blank=True)
    viber = models.CharField(max_length=100, blank=True)
    twitch = models.CharField(max_length=100,blank=True)
    instagram = models.CharField(max_length=100, blank=True)
    facebook = models.CharField(max_length=100, blank=True)
    twitter = models.CharField(max_length=100, blank=True)
    discord = models.CharField(max_length=100, blank=True)
    github = models.CharField(max_length=100, blank=True)
    youtube = models.CharField(max_length=100, blank=True)
    linkedin = models.CharField(max_length=100, blank=True)
    snapchat = models.CharField(max_length=100, blank=True)
    skype = models.CharField(max_length=100, blank=True)
    vk = models.CharField(max_length=100, blank=True)
    telegram = models.CharField(max_length=100,blank=True)
    phone = models.CharField(max_length=20,blank=True)

    def __str__(self):
        return f"{self.user.username}'s account"

    class Meta:
        ordering = ['user']
        verbose_name = 'Профиль'
        verbose_name_plural = 'Профили'


class FavoriteArticle(models.Model):
    user = models.ForeignKey(User,on_delete=models.SET_NULL,null=True)
    article = models.ForeignKey(Article,on_delete=models.SET_NULL,null=True)
    create_at=models.DateTimeField(auto_now_add=True)

class ContactForm(models.Model):
    status = models.BooleanField(default=False, verbose_name='Исправлено')
    name = models.CharField(verbose_name='Имя',max_length=100, validators = [MinLengthValidator(2)], null=False)
    email = models.EmailField(verbose_name='Адрес электронной почты',validators=[russian_email], null=False)
    message = RichTextField(verbose_name='Сообщение', null=False)

    class Meta:
        ordering = ['name']
        verbose_name = 'Форма обратной связи'
        verbose_name_plural = 'Форма обратной связи'