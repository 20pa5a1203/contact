from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('save_info',views.save_info,name='save_info'),
]
