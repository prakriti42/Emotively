# Generated by Django 4.0.3 on 2022-04-16 08:09

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('UMS', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dp', models.ImageField(default='default.jpg', upload_to='profile_pics')),
                ('firstname', models.CharField(max_length=120, verbose_name='First Name')),
                ('lastname', models.CharField(max_length=120, verbose_name='First Name')),
                ('contactNumber', phonenumber_field.modelfields.PhoneNumberField(max_length=128, region=None, unique=True, validators=[django.core.validators.RegexValidator(regex='^\\+?1?\\d{8,15}$')])),
                ('totalDetection', models.IntegerField(default=0)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]