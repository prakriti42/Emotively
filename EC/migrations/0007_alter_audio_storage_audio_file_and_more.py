# Generated by Django 4.0.3 on 2022-04-24 16:34

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('EC', '0006_alter_audio_storage_dateofupload'),
    ]

    operations = [
        migrations.AlterField(
            model_name='audio_storage',
            name='audio_file',
            field=models.FileField(upload_to='media'),
        ),
        migrations.AlterField(
            model_name='audio_storage',
            name='dateofUpload',
            field=models.DateField(default=datetime.datetime(2022, 4, 24, 16, 34, 54, 404054)),
        ),
    ]
