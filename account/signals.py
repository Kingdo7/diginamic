from django.contrib.auth.models import User
from django.db.models.signals import pre_save, post_save, pre_delete, post_delete

from .models import Profile


def user_receiver(sender, instance, created, *args, **kwargs):
    if created:
        Profile.objects.create(user=instance, first_name=instance.username)
post_save.connect(user_receiver, sender=User)