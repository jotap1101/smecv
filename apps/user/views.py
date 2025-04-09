from django.conf import settings
# from django.contrib import messages
from django.contrib.auth import get_user_model, views as auth_views
from django.contrib.auth.forms import PasswordResetForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.sites.shortcuts import get_current_site
from django.core.mail import EmailMessage
from django.shortcuts import redirect, render
from django.template.loader import render_to_string
from django.urls import reverse_lazy
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import force_bytes, force_str
from django.views import View
from django.views.generic import CreateView, TemplateView
from .forms import UserRegisterForm
from .tokens import account_activation_token

# Create your views here.
User = get_user_model()

def redirect_authenticated_user(request, redirect_url=None):
    if request.user.is_authenticated:
        return redirect(redirect_url or settings.LOGIN_REDIRECT_URL)
    
    return None

class LoginView(auth_views.LoginView):
    template_name = 'pages/user/login.html'
    redirect_authenticated_user = True

class LogoutView(auth_views.LogoutView, LoginRequiredMixin):
    template_name = 'pages/user/logout.html'

class RegisterView(CreateView):
    template_name = 'pages/user/register.html'
    form_class = UserRegisterForm
    success_url = reverse_lazy('user:register_done')
    
    def dispatch(self, request, *args, **kwargs):
        response = redirect_authenticated_user(request, 'core:home')

        return response if response else super().dispatch(request, *args, **kwargs)
    
    def form_valid(self, form):
        user = form.save(commit=False)
        user.is_active = False
        
        user.save()

        uidb64 = urlsafe_base64_encode(force_bytes(user.pk))
        token = account_activation_token.make_token(user)

        self.send_activation_email(user, uidb64, token)

        return super().form_valid(form)

    def send_activation_email(self, user, uidb64, token):
        current_site = get_current_site(self.request)
        mail_subject = 'Ative sua conta'
        message = render_to_string('emails/activation_email.html', {
            'user': user,
            'domain': current_site.domain,
            'protocol': 'https' if self.request.is_secure() else 'http',
            'uidb64': uidb64,
            'token': token,
        })
        email = EmailMessage(mail_subject, message, to=[user.email])

        email.send()

    
class ActivateAccountView(View):
    def get(self, request, uidb64, token):
        try:
            uid = force_str(urlsafe_base64_decode(uidb64))
            user = User.objects.get(pk=uid)
        except (TypeError, ValueError, OverflowError, User.DoesNotExist):
            user = None

        if user is not None and account_activation_token.check_token(user, token):
            user.is_active = True

            user.save()

            return render(request, 'pages/user/activation_success.html')
        else:
            return render(request, 'pages/user/activation_invalid.html')
        
class RegisterDoneView(TemplateView):
    template_name = 'pages/user/register_done.html'
    
    def dispatch(self, request, *args, **kwargs):
        response = redirect_authenticated_user(request, 'core:home')

        return response if response else super().dispatch(request, *args, **kwargs)
    
class PasswordResetView(auth_views.PasswordResetView):
    template_name = 'pages/user/password_reset.html'
    email_template_name = 'emails/password_reset_email.html'
    subject_template_name = 'emails/password_reset_subject.txt'
    success_url = reverse_lazy('user:password_reset_done')
    form_class = PasswordResetForm
    
    def dispatch(self, request, *args, **kwargs):
        response = redirect_authenticated_user(request, 'core:home')

        return response if response else super().dispatch(request, *args, **kwargs)

class PasswordResetDoneView(auth_views.PasswordResetDoneView):
    template_name = 'pages/user/password_reset_done.html'
    
    def dispatch(self, request, *args, **kwargs):
        response = redirect_authenticated_user(request, 'core:home')

        return response if response else super().dispatch(request, *args, **kwargs)

class PasswordResetConfirmView(auth_views.PasswordResetConfirmView):
    template_name = 'pages/user/password_reset_confirm.html'
    success_url = reverse_lazy('user:password_reset_complete')
    
    def dispatch(self, request, *args, **kwargs):
        response = redirect_authenticated_user(request, 'core:home')

        return response if response else super().dispatch(request, *args, **kwargs)

class PasswordResetCompleteView(auth_views.PasswordResetCompleteView):
    template_name = 'pages/user/password_reset_complete.html'

    def dispatch(self, request, *args, **kwargs):
        response = redirect_authenticated_user(request, 'core:home')

        return response if response else super().dispatch(request, *args, **kwargs)

class AccountProfileView(LoginRequiredMixin, TemplateView):
    template_name = 'pages/user/account_profile.html'

class AccountSecurityView(LoginRequiredMixin, TemplateView):
    template_name = 'pages/user/account_security.html'