# Generated by Django 3.2.6 on 2021-10-22 17:05

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('lostandfound', '0008_lostperson_per_reward_lost'),
    ]

    operations = [
        migrations.CreateModel(
            name='FoundPerson',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('per_name_found', models.CharField(max_length=50)),
                ('per_date_found', models.DateField()),
                ('per_location_found', models.CharField(max_length=50)),
                ('per_description_found', models.CharField(max_length=100)),
                ('per_picture_found', models.ImageField(blank=True, null=True, upload_to='media', verbose_name='Image')),
                ('per_number_found', models.CharField(max_length=50)),
                ('per_post_date_found', models.DateTimeField(default=django.utils.timezone.now)),
                ('per_age_found', models.IntegerField()),
                ('per_gender_found', models.CharField(max_length=50)),
                ('uploader', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
