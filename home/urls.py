from django.urls import path
from . import views

from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.WelcomeView.as_view(), name="welcome"),
    path('login/', views.LoginInterfaceView.as_view(), name="login"),
    path('logout/', views.LogoutInterfaceView.as_view(), name="logout"),
    path('signup/', views.SignupView.as_view(), name="signup"),

    path('change_password', views.ChangePassword, name="change_password"),
]