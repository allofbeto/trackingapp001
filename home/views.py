from django.http.response import HttpResponseRedirect
from django.views.generic import TemplateView
from django.views.generic.edit import CreateView
#this allows me to password protect pages
from django.contrib.auth.mixins import LoginRequiredMixin
#this imports the Django Login/out views
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.forms import UserCreationForm

from django.shortcuts import redirect

class PasswordRecoveryInterfaceView(TemplateView):
    template_name = "home/password_recovery.html"

class WelcomeView(TemplateView):
    template_name = "home/main.html"

class SignupView(CreateView):
    template_name = "home/signup.html"
    form_class = UserCreationForm
    success_url = '/workouts/login'

    def get(self, request, *args, **kwargs):
        if self.request.user.is_authenticated:
            return redirect('dashboard')
        return super().get(request, *args, **kwargs)

class LogoutInterfaceView(LogoutView):
    template_name = "home/splash.html"

class LoginInterfaceView(LoginView):
    TemplateView = "home/login.html"