# Generated by Django 4.0.2 on 2022-04-03 22:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('ActivityAPI', '0001_initial'),
        ('LoginAPI', '0001_initial'),
        ('LocationAPI', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Route',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('discription', models.CharField(max_length=300)),
                ('grade', models.CharField(max_length=16)),
                ('photo', models.ImageField(upload_to='Route_Images')),
                ('activity', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ActivityAPI.activity')),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('photo', models.ImageField(upload_to='Post_Images')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('likes', models.IntegerField(default=0)),
                ('text', models.CharField(default='', max_length=300)),
                ('activity', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='activity_post', to='ActivityAPI.activity')),
                ('location', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='location_post', to='LocationAPI.location')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_post', to='LoginAPI.user')),
            ],
        ),
    ]
