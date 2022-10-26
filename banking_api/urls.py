"""banking_api URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import path, include

from bank.views import loginView, registerView, optionsView, debitView, creditView, profileView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', loginView, name='login'),
    path('register/', registerView, name='register'),
    path('profile/<str:my_id>/', profileView, name='profile'),
    path('options/', optionsView, name='options'),
    path('credit/', creditView, name='credit'),
    path('debit/', debitView, name='debit')
]
