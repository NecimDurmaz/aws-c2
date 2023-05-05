from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("gozluk", views.glasses, name="glasses"),
    path("saat", views.watchs, name="watchs"),
    path("kahve", views.coffes, name="coffes"),
     path("deneme", views.deneme, name="deneme"),
]
