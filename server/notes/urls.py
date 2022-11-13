import uuid
from django.contrib import admin
from django.urls import path, include, register_converter
# from rest_framework.authtoken import views as token_views
from . import views
from .utils import HashIdConverter
from hashids import Hashids

register_converter(HashIdConverter, "hashid")

urlpatterns = [
    path('<hashid:pk>/', views.view_note, name='view-note'),
    path('save/', views.save_note, name='save-note'),
    path('save/<hashid:pk>/', views.save_note, name='save-note-specific')
]