# Generated by Django 5.1.2 on 2024-11-13 17:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0012_youtubevideo'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='YoutubeVideo',
            new_name='YoutubeVideoUrl',
        ),
    ]