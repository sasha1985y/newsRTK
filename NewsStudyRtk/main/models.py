from django.db import models

# Create your models here.
class News:
    def __init__(self, title, text, date):
        self.title = title
        self.text = text
        self.date = date

    def __str__(self):
        return f'{self.title}: {self.text}, {self.date}'
