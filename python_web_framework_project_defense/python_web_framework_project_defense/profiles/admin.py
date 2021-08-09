from django.contrib import admin

# Register your models here.
from python_web_framework_project_defense.profiles.models import Profile


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    pass
