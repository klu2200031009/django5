"""
URL configuration for TTM project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.urls import path, include
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", views.homePage, name="home"),
    path("login", views.loginPage, name="login"),
    path("contactus", views.contactPage, name="contact"),
    path("aboutus", views.aboutPage, name="about"),
    path("Register", views.registrationPage, name="register"),
    path("insert", views.insertpage, name="insert"),
    path("update",views.updatepage,name="update"),
    path("delete",views.deletepage,name="delete"),
    path("insertvehicle",views.insertvehiclepage,name="insertvehicle"),
    path("updatevehicle",views.updatevehiclepage,name="updatevehicle"),
    path("deletevehicle",views.deletevehiclepage,name="deletevehicle"),
    path("feedback",views.feedbackpage,name="feedback"),
    path("payment",views.paymentpage,name="payment"),
    path("", include("adminapp.urls")),

]
