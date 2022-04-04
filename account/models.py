from django.db import models

# Create your models here.

from django.urls import reverse
from django.contrib.auth.models import User
from django.utils.text import slugify
from django.utils.crypto import get_random_string


class Profile(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='userprofile')
    point = models.PositiveIntegerField(default=10)
    bio = models.CharField(max_length=2000)
    first_name = models.CharField(max_length=500)
    last_name = models.CharField(max_length=500)
    following = models.ManyToManyField(User, related_name="following")
    follower = models.ManyToManyField(User, related_name="follower")
    waitinglist = models.ManyToManyField(User, related_name="waitinglist")
    slug = models.SlugField(null=True, blank=True)

    def __str__(self):
        return str(self.user) or ""

    def get_absolute_url(self):
        return reverse('account:profile-detail', kwargs={'slug': self.slug})

    def get_follower_list_count(self):
        return len(self.follower.all())

    def get_friend_list_count(self):
        return len(self.friendlist.all())

    def get_waiting_list(self):
        return self.waitinglist.all()

    def save(self, *args, **kwargs):
        if self.slug:
            super(Profile, self).save(*args, **kwargs)
        else:
            self.slug = slugify(str(self.user) + get_random_string(9))
            super(Profile, self).save(*args, **kwargs)


class Friend(models.Model):

    profile = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name="friendlist")
    friend = models.OneToOneField(User, on_delete=models.CASCADE, related_name="friend")
    is_accepted = models.BooleanField(default=False)
    slug = models.SlugField(null=True, blank=True)

    def __str__(self):
        return str(self.profile) or ""

    def get_absolute_url(self):
        return reverse('account:profile-detail', kwargs={'slug': self.slug})

    def save(self, *args, **kwargs):
        if self.slug:
            super(Friend, self).save(*args, **kwargs)
        else:
            self.slug = slugify(str(self.profile) + get_random_string(9))
            super(Friend, self).save(*args, **kwargs)

