# Generated by Django 5.1.2 on 2024-11-11 14:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0006_team'),
    ]

    operations = [
        migrations.CreateModel(
            name='Banner',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('video_banner', models.FileField(upload_to='videos/')),
            ],
        ),
        migrations.RemoveField(
            model_name='video',
            name='video_file',
        ),
        migrations.AddField(
            model_name='video',
            name='youtube_url',
            field=models.URLField(blank=True, null=True),
        ),
    ]
