from django.contrib import messages
from django.contrib.auth import  get_user_model, views as auth_views
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm, PasswordResetForm
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView
from .forms import UserLoginForm, UserRegisterForm

# Create your views here.
User = get_user_model()

class LoginView(auth_views.LoginView):
    template_name = 'pages/user/login.html'
    redirect_authenticated_user = True

class LogoutView(auth_views.LogoutView):
    template_name = 'pages/user/logout.html'
    redirect_authenticated_user = True

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            messages.error(request, 'You are not logged in.')
            return redirect('user:login')
        
        return super().dispatch(request, *args, **kwargs)

class RegisterView(CreateView):
    template_name = 'pages/user/register.html'
    form_class = UserRegisterForm
    
    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('core:home')
        
        return super().dispatch(request, *args, **kwargs)
    
class PasswordResetView(auth_views.PasswordResetView):
    template_name = 'pages/user/password_reset.html'
    email_template_name = 'emails/password_reset_email.html'
    # subject_template_name = 'pages/user/password_reset_subject.txt'
    success_url = reverse_lazy('user:password_reset_done')
    form_class = PasswordResetForm
    redirect_authenticated_user = True

class PasswordResetDoneView(auth_views.PasswordResetDoneView):
    template_name = 'pages/user/password_reset_done.html'
    redirect_authenticated_user = True

class PasswordResetConfirmView(auth_views.PasswordResetConfirmView):
    template_name = 'pages/user/password_reset_confirm.html'
    success_url = reverse_lazy('user:password_reset_complete')
    redirect_authenticated_user = True

class PasswordResetCompleteView(auth_views.PasswordResetCompleteView):
    template_name = 'pages/user/password_reset_complete.html'
    redirect_authenticated_user = True