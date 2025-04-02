from django.contrib import messages
from django.contrib.auth import authenticate, get_user, get_user_model, login, logout, views as auth_views
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse_lazy
from .forms import UserLoginForm, UserRegisterForm

# Create your views here.
User = get_user_model()

class CustomLoginView(auth_views.LoginView):
    # form_class = UserLoginForm
    template_name = 'pages/login.html'
    redirect_authenticated_user = True

    def get_success_url(self) -> str:
        return super().get_success_url()
    
    def form_valid(self, form: auth_views.AuthenticationForm) -> HttpResponse:
        return super().form_valid(form)
    
    def form_invalid(self, form: auth_views.AuthenticationForm) -> HttpResponse:
        return super().form_invalid(form)

class CustomLogoutView(auth_views.LogoutView):
    template_name = 'pages/logout.html'
    
class CustomRegisterView(auth_views.FormView):
    form_class = UserRegisterForm
    template_name = 'pages/register.html'
    success_url = reverse_lazy('user:login')

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)