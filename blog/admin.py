from django.contrib import admin

from .models import User, Profile, Blog, Likes
# Register your models here.

admin.site.register((User, Profile, Blog, Likes))
