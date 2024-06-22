from django.contrib import admin
from django.urls import path
from home import views

urlpatterns = [
    path('', views.signup, name='signup'),
     path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),
    path('main/',views.main,name='main'),
]