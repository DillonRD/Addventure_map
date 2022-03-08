# Generated by Django 4.0.2 on 2022-03-08 02:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('AdminAPI', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='activity',
            name='location',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='activity_location', to='AdminAPI.location'),
        ),
        migrations.DeleteModel(
            name='Post',
        ),
    ]
