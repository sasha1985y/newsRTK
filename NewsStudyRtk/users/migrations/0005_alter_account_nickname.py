# Generated by Django 4.2.6 on 2023-12-21 21:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_alter_account_address_alter_account_job_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='account',
            name='nickname',
            field=models.CharField(max_length=100),
        ),
    ]