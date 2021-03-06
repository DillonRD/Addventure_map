# Generated by Django 4.0.2 on 2022-05-03 20:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('LocationAPI', '0004_rename_latitude_location_lat_and_more'),
        ('ActivityAPI', '0003_activity_location'),
    ]

    operations = [
        migrations.AlterField(
            model_name='activity',
            name='location',
            field=models.ForeignKey(db_constraint=False, on_delete=django.db.models.deletion.CASCADE, to='LocationAPI.location'),
        ),
    ]
