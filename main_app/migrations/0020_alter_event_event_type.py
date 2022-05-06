# Generated by Django 4.0.4 on 2022-05-05 23:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0019_remove_photo_types_alter_event_event_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='event_type',
            field=models.CharField(choices=[('L', 'Lunar'), ('S', 'Solar'), ('C', 'Conjunction'), ('P', 'Planetary'), ('M', 'Meteor'), ('C', 'Comet'), ('AD', 'Asteroid'), ('AM', 'Astronomy'), ('SC', 'Spacecraft')], default='L', max_length=10),
        ),
    ]