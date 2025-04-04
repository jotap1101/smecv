from django.urls import path
from .views import *
from django.contrib.auth import views as auth_views

app_name = 'user'

urlpatterns = [
    # path('auth/login/', auth_views.LoginView.as_view(template_name='pages/user/login.html'), name='login'),
    # path('auth/logout/', auth_views.LogoutView.as_view(template_name='pages/user/logout.html'), name='logout'),
    path('auth/login/', LoginView.as_view(), name='login'),
    path('auth/logout/', LogoutView.as_view(), name='logout'),
    path('auth/register/', RegisterView.as_view(), name='register'),

    path('auth/password_reset/', PasswordResetView.as_view(), name='password_reset'),
    path('auth/password_reset/done/', PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('auth/reset/<uidb64>/<token>/', PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('auth/reset/done/', PasswordResetCompleteView.as_view(), name='password_reset_complete'),
]