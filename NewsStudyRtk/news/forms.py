from django import forms
from django.core.validators import MinLengthValidator

from django.forms import ModelForm, Textarea, CheckboxSelectMultiple,Select
from .models import Article

class ArticleForm(ModelForm):
    class Meta:
        model = Article
        fields = ['title','anouncement','text','tags']
        widgets = {
            'anouncement': Textarea(attrs={'cols':80,'rows':2}),
            'text': Textarea(attrs={'cols': 80, 'rows': 2}),
            'tags': CheckboxSelectMultiple()
        }