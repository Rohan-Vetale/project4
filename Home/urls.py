from django.contrib import admin
from django.urls import path
from Home import views

urlpatterns = [
    path('', views.home, name="HomePage"),
    path('about/', views.about, name="About"),
    path('app1/', views.app1, name="App1"),
    path('search/', views.search, name="Search Page")
]
