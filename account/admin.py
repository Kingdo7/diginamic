from django.contrib import admin

# Register your models here.
from .models import Profile, Friend

class FriendAdmin(admin.ModelAdmin):
    list_display = ['profile', 'friend', 'is_accepted']

class ProfileAdmin(admin.ModelAdmin):
    list_display = ['user', 'point', 'bio', 'first_name', 'last_name']



admin.site.register(Profile, ProfileAdmin)
admin.site.register(Friend, FriendAdmin)
