"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
import smtplib

app_name = 'main'

urlpatterns = [
	path("", views.homepage, name = "Homepage"),
	path("login/", views.login_request, name = "Login"),
	path("register/", views.register, name="register"),
    path("logout/", views.logout_request, name= "Logout"),
    path(
        'admin/password_reset/',
        auth_views.PasswordResetView.as_view(template_name = 'main/Reset.html'),
        name='admin_password_reset',
    ),
    path(
        'admin/password_sent/',
        auth_views.PasswordResetDoneView.as_view(template_name = 'main/password_sent.html'),
        name='admin_password_sent',
    ),
    path(
        'password_reset/<uidb64>/<token>/',
        auth_views.PasswordResetConfirmView.as_view(),
        name='password_confirm',
    ),
    path(
        'reset/done/',
        auth_views.PasswordResetCompleteView.as_view(template_name = 'main/password_complete.html'),
        name='password_complete',
    ),
]

