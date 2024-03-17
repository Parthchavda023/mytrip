from django.contrib import admin
from django.urls import path
from l_app import views

urlpatterns = [
    path('', views.index),
    path('feedback/', views.feedback, name='feedback'),
    path('about/', views.about),
    path('contact/', views.contact),
    path('update/', views.update_profile),
    path('logout/', views.user_logout),
    path('otp/', views.otpverify, name='otpverify'),
]