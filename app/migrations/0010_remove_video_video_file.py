# Generated by Django 5.1.2 on 2024-11-11 18:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0009_video_youtube_url'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='video',
            name='video_file',
        ),
    ]
