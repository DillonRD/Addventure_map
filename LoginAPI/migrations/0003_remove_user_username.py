# Generated by Django 4.0.3 on 2022-04-07 15:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('LoginAPI', '0002_remove_user_confirmpassword'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='username',
        ),
    ]
