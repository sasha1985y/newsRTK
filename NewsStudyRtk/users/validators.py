from django.core.validators import ValidationError
from django.utils.translation import gettext_lazy as _

def russian_email(email):
    allowed_domains = ['@mail.ru',
                       '@bk.ru',
                       '@yandex.ru']
    if not any(domain in email for domain in allowed_domains):
        raise ValidationError(
            _("%(email) has not allowed domain"),params={'email':email}
        )

def clean_username(username):
    username = username.cleaned_data['username']
    if len(username) < 2:
        raise ValidationError('Имя пользователя не может быть меньше 2 знаков')
    return username