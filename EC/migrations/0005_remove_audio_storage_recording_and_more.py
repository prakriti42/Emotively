# Generated by Django 4.0.3 on 2022-04-24 16:11

import datetime
import django.core.files.storage
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('EC', '0004_alter_audio_storage_recording_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='audio_storage',
            name='recording',
        ),
        migrations.RemoveField(
            model_name='audio_storage',
            name='timeToUpload',
        ),
        migrations.AddField(
            model_name='audio_storage',
            name='audio_file',
            field=models.FileField(default=1, storage=django.core.files.storage.FileSystemStorage(location='/home/prakriti/College/FYP/Project/Emotively/media'), upload_to=''),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='audio_storage',
            name='recordingname',
            field=models.CharField(default='Unknown', max_length=100),
        ),
        migrations.AlterField(
            model_name='audio_storage',
            name='Tag',
            field=models.CharField(blank=True, default='Untagged', max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='audio_storage',
            name='dateofUpload',
            field=models.DateField(default=datetime.datetime(2022, 4, 24, 16, 10, 51, 194949, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='audio_storage',
            name='duration',
            field=models.FloatField(default=0.0),
        ),
    ]
