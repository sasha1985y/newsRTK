from django.db import models
from django.forms import forms
# Create your models here.
from django.utils.safestring import mark_safe

# Create your models here.
# class Link:
#     def __init__(self, text):
#         self.text = text
#
#     def content(self):
#         return self.text
#
class Demo(models.Model):
    title = models.CharField(max_length=30)
    image = models.ImageField(blank = True, upload_to='images/')

    def __str__(self):
        return self.title

    def image_tag(self):
        if self.image is not None:
            return mark_safe('<img src="{}" height="50"/>'.format(self.image.url))