from django.urls import path
from django.contrib.auth.views import LoginView, logout_then_login
from . import views

urlpatterns = [
    path("login/", LoginView.as_view(template_name='login.html'), name="login"),
    path("signup/", views.SignUpView.as_view(), name="signup"),
    path("logout/", logout_then_login, name="logout"),
]