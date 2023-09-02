from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.forms import SetPasswordForm
from django.contrib import messages
from django.shortcuts import render, redirect
from django.views.generic import TemplateView, CreateView
from .forms import CustomUserCreationForm


class WelcomeView(TemplateView):
    template_name = "home/main.html"


class SignupView(CreateView):
    template_name = "home/signup.html"
    form_class = CustomUserCreationForm
    success_url = '/workouts/login'

    def get(self, request, *args, **kwargs):
        if self.request.user.is_authenticated:
            return redirect('/workouts/create-category/')
        return super().get(request, *args, **kwargs)


class LogoutInterfaceView(LogoutView):
    template_name = "home/splash.html"


class LoginInterfaceView(LoginView):
    template_name = "workouts/login.html"  # Use 'template_name', not 'TemplateView'


@login_required
def ChangePassword(request):
    user = request.user
    if request.method == 'POST':
        form = SetPasswordForm(user, request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Your password has been changed!")
            return redirect('dashboard')  # Make sure 'dashboard' is the correct URL name
        else:
            for error in list(form.errors.values()):
                messages.error(request, error)

    form = SetPasswordForm(user)
    return render(request, 'home/password_reset_confirm.html', {'form': form})
