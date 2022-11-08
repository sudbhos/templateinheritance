
from django.contrib import admin
from django.urls import path,include
from .import views
urlpatterns = [
    path("",views.sport,name="sport"),
    path("home",views.home,name="home"),
    path("movie",views.movie,name="movie"),
    path("politics",views.politics,name="politics")
]
