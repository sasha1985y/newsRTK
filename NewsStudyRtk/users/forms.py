from django import forms
from .validators import russian_email
from django.core.validators import MinLengthValidator

from django.contrib.auth.forms import UserChangeForm
from django.contrib.auth.models import User
from django.forms import TextInput, EmailInput, FileInput, DateInput

class UserUpdateForm(UserChangeForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name']
        widgets = {'username': TextInput({'class': 'textinput form-control',
                                          'placeholder': 'username'}),
                   'email': EmailInput({'class': 'textinput form-control',
                                        'placeholder': 'email'}),
                   'first_name': TextInput({'class': 'textinput form-control',
                                            'placeholder': 'First name'}),
                   'last_name': TextInput({'class': 'textinput form-control',
                                           'placeholder': 'Last name'}),
                   }


from .models import Account
class AccountUpdateForm(forms.ModelForm):
    birthdate = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}), required=False)
    class Meta:
        model = Account
        fields = ['phone', 'address','job','vk','telegram', 'account_image','nickname','birthdate']
        widgets = {'phone': TextInput({'class': 'textinput form-control',
                                       'placeholder': 'phone number'}),
                   'address': TextInput({'class': 'textinput form-control',
                                         'placeholder': 'address'}),
                   'job': TextInput({'class': 'textinput form-control',
                                         'placeholder': 'job'}),
                   'vk': TextInput({'class': 'textinput form-control',
                                      'placeholder': 'vk'}),
                   'telegram': TextInput({'class': 'textinput form-control',
                                           'placeholder': 'telegram'}),
                   'account_image': FileInput({'class': 'form-control',
                                       'placeholder': 'image'}),
                   'nickname': TextInput({'class': 'textinput form-control',
                                            'placeholder': 'nickname'}),
                   'birthdate': DateInput(attrs={'type': 'date'}),
                   }

class ContactForm(forms.Form):
    name = forms.CharField(max_length=100,
                           validators = [MinLengthValidator(2)],
                           initial='Имя')
    email = forms.EmailField(validators=[russian_email])
    message = forms.CharField(widget=forms.TextInput, disabled=False)
    demo = forms.BooleanField(required = False, help_text='Текст-подсказка',
                              label='Вам нравится?',
                              initial=True)

    # name = forms.CharField(max_length=100)
    # email = forms.EmailField()
    # message = forms.CharField(widget=forms.Textarea)