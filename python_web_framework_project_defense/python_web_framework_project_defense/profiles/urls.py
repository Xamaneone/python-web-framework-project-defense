from django.urls import path

from python_web_framework_project_defense.profiles.views import profile_edit, profile_details

urlpatterns = (
    path('<int:pk>', profile_details, name='profile'),
    path('edit/<int:pk>', profile_edit, name='edit profile')
)

import python_web_framework_project_defense.profiles.signals

