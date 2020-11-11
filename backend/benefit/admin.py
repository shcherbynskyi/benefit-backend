from django.contrib import admin
from .models import *


@admin.register(AppConfig)
class AppConfigAdmin(admin.ModelAdmin):
    pass


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('__str__', 'height', 'weight', 'date_of_birth', 'gender')
