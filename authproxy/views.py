from django.shortcuts import render,redirect
from django.views.generic import CreateView, TemplateView
from .models import Profile

class ProfileCreate(CreateView):
    model = Profile
    fields = ['username','first_name','last_name','email','password']
    success_url = 'success'

class ProfileSuccess(TemplateView):
    template_name = 'success.html'

