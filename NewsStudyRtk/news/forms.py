from django import forms
from django.forms import inlineformset_factory
from django.core.validators import ValidationError
from django.forms import ModelForm, Textarea, CheckboxSelectMultiple,Select
from .models import *

class MultipleFileInput(forms.ClearableFileInput):
    allow_multiple_selected = True


class MultipleFileField(forms.FileField):
    def __init__(self, *args, **kwargs):
        kwargs.setdefault("widget", MultipleFileInput())
        super().__init__(*args, **kwargs)

    def clean(self, data, initial=None):
        single_file_clean = super().clean
        if isinstance(data, (list, tuple)):
            result = [single_file_clean(d, initial) for d in data]
        else:
            result = single_file_clean(data, initial)
        return result

class SubscribeForm(forms.ModelForm):
    class Meta:
        model = Subscriber
        fields = '__all__'
        widgets = {
            'last_name': Textarea(attrs={'cols': 96, 'rows': 1}),
            'first_name': Textarea(attrs={'cols': 101, 'rows': 1}),
        }

    def clean_last_name(self):
        last_name = self.cleaned_data['last_name']
        if not last_name:
            raise ValidationError('Last name is required')
        return last_name

    def clean_first_name(self):
        first_name = self.cleaned_data['first_name']
        if not first_name:
            raise ValidationError('First name is required')
        return first_name

    def clean_email(self):
        email = self.cleaned_data['email']
        if not email:
            raise ValidationError('Email is required')
        return email

    def save(self):
        last_name = self.cleaned_data['last_name']
        first_name = self.cleaned_data['first_name']
        email = self.cleaned_data['email']
        Subscriber.objects.create(last_name=last_name, first_name=first_name, email=email)

    def clean_last_name(self):
        last_name = self.cleaned_data['last_name']
        if len(last_name) < 2:
            raise ValidationError('Фамилия не может быть меньше 2 знаков')
        return last_name

    def clean_first_name(self):
        first_name = self.cleaned_data['first_name']
        if len(first_name) < 2:
            raise ValidationError('Имя не может быть меньше 2 знаков')
        return first_name

ImagesFormSet = inlineformset_factory(Article, Image, fields=("image",),extra=1,max_num=1,
    widgets={
        "image_field": MultipleFileField(),
    })


class ArticleForm(ModelForm):
    image_field = MultipleFileField()
    class Meta:
        model = Article
        fields = ['title',
                  'anouncement',
                  'text',
                  'tags',
                  'category',
                  'source',
                  'sourcename',
                  ]
        widgets = {
            'category': Select(choices=[(x[0], x[1]) for x in Article.categories]),
            'title': Textarea(attrs={'cols': 80, 'rows': 1}),
            'anouncement': Textarea(attrs={'cols': 87, 'rows': 7}),
            'source': Textarea(attrs={'cols': 88, 'rows': 1}),
            'sourcename': Textarea(attrs={'cols': 78, 'rows': 1}),
            'tags': CheckboxSelectMultiple(),
        }

class ArticleRequestForm(ModelForm):
    image_field = MultipleFileField()
    class Meta:
        model = Article
        fields = ['title',
                  'anouncement',
                  'text',
                  'category',
                  'source',
                  'sourcename',
                  ]
        widgets = {
            'category': Select(choices=[(x[0], x[1]) for x in Article.categories]),
            'title': Textarea(attrs={'cols': 80, 'rows': 1}),
            'anouncement': Textarea(attrs={'cols': 87, 'rows': 7}),
            'source': Textarea(attrs={'cols': 88, 'rows': 1}),
            'sourcename': Textarea(attrs={'cols': 78, 'rows': 1}),
        }