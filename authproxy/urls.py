from django.contrib import admin
from django.urls import path
from .views import ProfileCreate, ProfileSuccess

urlpatterns = [
    path('create', ProfileCreate.as_view(), name='create'),
    path('success', ProfileSuccess.as_view(), name='success'),
]
