# Generated by Django 3.1.2 on 2020-11-09 05:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('CarApp', '0017_producttable_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='producttable',
            name='image',
        ),
    ]