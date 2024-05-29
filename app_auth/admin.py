from django.contrib import admin

from app_auth.models import *

# Register your models here.

class ProfileAdmin(admin.ModelAdmin):
    pass

admin.site.register(Profile, ProfileAdmin)