from django.urls import path

from . import views


urlpatterns = [
    path("ttmhome", views.ttmhome, name="ttmhome"),
    path("checkadminlogin", views.checkadminlogin, name="checkadminlogin"),
    path("checkregistration", views.checkregistration, name="checkregistration"),
    path("checkinsert", views.checkinsert, name="checkinsert"),
    path("checkupdate",views.checkupdate, name="checkupdate"),
    path("checkdelete",views.checkdelete, name="checkdelete"),
    path("checkinsertvehicle",views.checkinsertvehicle, name="checkinsertvehicle"),
    path("checkupdatevehicle",views.checkupdatevehicle, name="checkupdatevehicle"),
    path("checkdeletevehicle",views.checkdeletevehicle, name="checkdeletevehicle"),
    path("feedback",views.checkfeedback, name="checkfeedback"),
    path("checkhome", views.checkhome, name="checkhome"),
    path("about/", views.checkabout, name="checkabout"),
    path("adminhome/",views.adminhome,name="adminhome"),


]
