# Generated by Django 4.2.3 on 2023-07-26 12:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('settings', '0009_video_alter_announcement_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='video',
            name='poster',
            field=models.ImageField(default=1, upload_to='poster/'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='video',
            name='video',
            field=models.FileField(upload_to='video/'),
        ),
    ]