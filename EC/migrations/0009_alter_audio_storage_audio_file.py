# Generated by Django 4.0.3 on 2022-04-24 18:06

import django.core.files.storage
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('EC', '0008_alter_audio_storage_audio_file_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='audio_storage',
            name='audio_file',
            field=models.FileField(storage=django.core.files.storage.FileSystemStorage(location='/home/prakriti/College/FYP/Project/Emotively/media'), upload_to=''),
        ),
    ]
