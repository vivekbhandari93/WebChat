from django.shortcuts import render
from .forms import MemberForm
from .models import Member
from django.views.generic import CreateView, DetailView, DeleteView, UpdateView
from django.urls import reverse_lazy
from braces.views import SelectRelatedMixin
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages

class Signup(CreateView):
    form_class = MemberForm
    template_name = 'accounts/signup.html'
    success_url = reverse_lazy('accounts:login')


class ProfileDetail(DetailView, LoginRequiredMixin):
    model = Member

    def get_queryset(self):
        query =  super().get_queryset()
        return query.filter(slug=self.kwargs.get('slug'))


class AccountDelete(DeleteView, LoginRequiredMixin):
    model = Member
    success_url = reverse_lazy('accounts:signup')   

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.filter(slug=self.kwargs.get('slug'))
    
    def delete(self, *args, **kwargs):
        messages.success(self.request,'Post Deleted')
        return super().delete(*args, **kwargs)


class ProfileUpdate(UpdateView, LoginRequiredMixin):
    fields = ('profile_pic', 'about', 'website')
    model = Member
