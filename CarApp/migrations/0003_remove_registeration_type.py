# Generated by Django 3.1.2 on 2020-10-28 12:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('CarApp', '0002_logintable'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='registeration',
            name='type',
        ),
    ]
