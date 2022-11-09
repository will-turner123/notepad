import uuid
from django.contrib import admin
from django.urls import path, include
# from rest_framework.authtoken import views as token_views
from . import views

urlpatterns = [
    path('<int:pk>/', views.view_note, name='note')
]