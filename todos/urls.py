from django.contrib import admin
from django.urls import path, include
from todos import views

# http://127.0.0.1:8000/admin/
urlpatterns = [
    path("", views.home, name="home"),  # dev_1
]
