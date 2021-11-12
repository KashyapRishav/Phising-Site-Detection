from django.contrib import admin
from django.urls import path
from authPart import views

urlpatterns = [
    path("", views.index,name= "index"),
    path('check', views.home,name= "home"),
    path('contact', views.contact,name= "contact"),
    path("logout", views.handleLogout,name="handleLogout"),
    path("signup", views.handleSignup,name="handleSignup"),
    path("login", views.handleLogin,name="handleLogout"),
    path('result/', views.result,name= "result"),
]
