# Generated by Django 3.1.2 on 2020-11-14 05:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CarApp', '0028_auto_20201114_1054'),
    ]

    operations = [
        migrations.AddField(
            model_name='customerfeedback',
            name='updated',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='customerfeedback',
            name='date',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]