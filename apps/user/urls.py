from django.urls import path
from .views import CustomLoginView, CustomLogoutView, CustomRegisterView

app_name = 'user'

urlpatterns = [
    path('auth/login/', CustomLoginView.as_view(), name='login'),
    path('auth/logout/', CustomLogoutView.as_view(), name='logout'),
    path('auth/register/', CustomRegisterView.as_view(), name='register'),
]