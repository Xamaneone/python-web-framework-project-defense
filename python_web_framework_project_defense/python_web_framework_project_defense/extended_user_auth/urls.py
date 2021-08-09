from django.urls import path

from python_web_framework_project_defense.extended_user_auth.views import register, log_in, log_out

urlpatterns = (
    path('register/', register, name='register'),
    path('login/', log_in, name='login'),
    path('logout/', log_out, name='logout'),
)


