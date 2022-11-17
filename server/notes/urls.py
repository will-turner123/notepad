import uuid
from django.contrib import admin
from django.urls import path, include, register_converter
# from rest_framework.authtoken import views as token_views
from . import views


urlpatterns = [
    path('get/<str:note_id>/', views.view_note, name='view-note'),
    path('create/', views.create_note, name='create-note'),
]