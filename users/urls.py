from django.urls import path
from .views import register, profile, logout_view
from django.contrib.auth.views import LoginView

urlpatterns = [
    path('register/', register, name='register'),
    path('login/', LoginView.as_view(template_name='users/login.html'), name='login'),
    path('profile/', profile, name='profile'),
    path('logout/', logout_view, name='logout')
]