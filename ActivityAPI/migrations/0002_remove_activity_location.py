# Generated by Django 4.0.2 on 2022-05-03 20:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ActivityAPI', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='activity',
            name='location',
        ),
    ]
