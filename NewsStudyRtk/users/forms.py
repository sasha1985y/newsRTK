from django import forms
#from .validators import russian_email
from django.core.validators import MinLengthValidator

class ContactForm(forms.Form):
    # name = forms.CharField(max_length=100,
    #                        validators = [MinLengthValidator(2)],
    #                        initial='Имя')
    # email = forms.EmailField(validators=[russian_email])
    # message = forms.CharField(widget=forms.TextInput, disabled=False)
    # demo = forms.BooleanField(required = False, help_text='Текст-подсказка',
    #                           label='Вам нравится?',
    #                           initial=True)

    name = forms.CharField(max_length=100)
    email = forms.EmailField()
    message = forms.CharField(widget=forms.Textarea)