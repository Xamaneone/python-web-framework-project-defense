from django.urls import path

from python_web_framework_project_defense.profiles.views import profile_edit

urlpatterns = (
    path('profile/', profile_edit, name='profile'),
)

import python_web_framework_project_defense.profiles.signals

