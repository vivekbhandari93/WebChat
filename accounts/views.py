from django.shortcuts import render
from .forms import UserForm
from django.views.generic import CreateView
from django.urls import reverse_lazy


class Signup(CreateView):
    form_class = UserForm
    template_name = 'accounts/signup.html'
    success_url = reverse_lazy('login')
