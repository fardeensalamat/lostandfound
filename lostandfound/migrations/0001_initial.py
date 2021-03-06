# Generated by Django 3.2.6 on 2021-10-19 16:41

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='LostPet',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('animal_lost', models.CharField(max_length=50)),
                ('breed_lost', models.CharField(max_length=30)),
                ('color_lost', models.CharField(max_length=30)),
                ('location_lost', models.CharField(max_length=30)),
                ('description_lost', models.TextField()),
                ('reward_pet_lost', models.CharField(max_length=5)),
                ('date_lost', models.DateField()),
                ('post_date_lost', models.DateTimeField(default=django.utils.timezone.now)),
                ('number_lost', models.BigIntegerField()),
                ('uploader', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
