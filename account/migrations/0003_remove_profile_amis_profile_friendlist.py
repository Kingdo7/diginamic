# Generated by Django 4.0.3 on 2022-03-28 09:05

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('account', '0002_profile_amis'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='amis',
        ),
        migrations.AddField(
            model_name='profile',
            name='friendlist',
            field=models.ManyToManyField(to=settings.AUTH_USER_MODEL),
        ),
    ]
