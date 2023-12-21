from django.db import models
from django.contrib.auth.models import User
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
    vk = models.CharField(max_length=100,blank=True)
    telegram = models.CharField(max_length=100,blank=True)
    phone = models.CharField(max_length=20,blank=True)

    def __str__(self):
        return f"{self.user.username}'s account"

    class Meta:
        ordering = ['user']
        verbose_name = 'Профиль'
        verbose_name_plural = 'Профили'