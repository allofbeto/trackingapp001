from django.http.response import HttpResponseRedirect
from django.views.generic import TemplateView
from django.views.generic.edit import CreateView
#this allows me to password protect pages
from django.contrib.auth.mixins import LoginRequiredMixin
#this imports the Django Login/out views
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.forms import UserCreationForm

from django.shortcuts import redirect, render

from Workouts.forms import SetPasswordForm,PasswordResetForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .decorators import user_not_authenticated

from .forms import CustomUserCreationForm



class WelcomeView(TemplateView):
    template_name = "home/main.html"

class SignupView(CreateView):
    template_name = "home/signup.html"
    form_class = CustomUserCreationForm
    success_url = '/workouts/login'

    def get(self, request, *args, **kwargs):
        if self.request.user.is_authenticated:
            return redirect('dashboard')
        return super().get(request, *args, **kwargs)

class LogoutInterfaceView(LogoutView):
    template_name = "home/splash.html"

    def send_simple_message():
        return requests.post(
            "https://api.mailgun.net/v3/sandboxa7e9d238ad5340fc996146bdb04d2088.mailgun.org/messages",
            auth=("api", "<73f745ed-615b1ade>"),
            data={"from": "Mailgun Sandbox <postmaster@sandboxa7e9d238ad5340fc996146bdb04d2088.mailgun.org>",
                  "to": "Alberto Carrazco <carrazco2013@gmail.com>",
                  "subject": "Hello Alberto Carrazco",
                  "text": "Congratulations Alberto Carrazco, you just sent an email with Mailgun!  You are truly awesome!"})

class LoginInterfaceView(LoginView):
    TemplateView = "home/login.html"

@login_required
def ChangePassword(request):
    user = request.user
    if request.method == 'POST':
        form = SetPasswordForm(user, request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Your password has been changed!")
            return redirect('dashboard')
        else:
            for error in list(form.errors.values()):
                messages.error(request, error)

    form = SetPasswordForm(user)
    return render(request, 'home/password_reset_confirm.html', {'form':form})

