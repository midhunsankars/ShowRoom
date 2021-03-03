# Generated by Django 3.1.2 on 2020-11-14 05:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CarApp', '0026_auto_20201111_1529'),
    ]

    operations = [
        migrations.CreateModel(
            name='CustomerFeedBack',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cname', models.CharField(max_length=300)),
                ('feedback', models.CharField(max_length=500)),
                ('date', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'db_table': 'CustomerFeedBack',
            },
        ),
    ]
