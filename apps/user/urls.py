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

    path('account/activate/<uidb64>/<token>/', ActivateAccountView.as_view(), name='activate'),
    path('account/activate/done/', RegisterDoneView.as_view(), name='register_done'),
    path('account/profile/', AccountProfileView.as_view(), name='profile'),
    path('account/password/change/', PasswordChangeView.as_view(), name='password_change'),

    path('password/reset/', PasswordResetView.as_view(), name='password_reset'),
    path('password/reset/done/', PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('password/reset/confirm/<uidb64>/<token>/', PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('password/reset/complete/', PasswordResetCompleteView.as_view(), name='password_reset_complete'),
]