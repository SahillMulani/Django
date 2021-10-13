from django.urls import path

from . import views

urlpatterns = [
    path("<str:names>",views.index,name="index"),
    path("",views.home,name="home"),
]