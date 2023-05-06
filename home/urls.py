from django.urls import path
from . import views

urlpatterns = [
    path('', views.WelcomeView.as_view(), name="welcome"),
    path('login/', views.LoginInterfaceView.as_view(), name="login"),
    path('logout/', views.LogoutInterfaceView.as_view(), name="logout"),
    path('password-recovery', views.PasswordRecoveryInterfaceView.as_view(), name="password-recovery"),
    path('signup/', views.SignupView.as_view(), name="signup"),
]