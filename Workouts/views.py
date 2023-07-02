from datetime import datetime
from django.http.response import HttpResponseRedirect
from django.template.context_processors import request

#this imports the models I've created
from .models import Exercises,Entry, Days
#this allows me to create/edit/delete model entries
from django.views.generic import CreateView, UpdateView, TemplateView, ListView, DetailView
from django.views.generic.edit import DeleteView
#this allows me to password protect pages
from django.contrib.auth.mixins import LoginRequiredMixin
#This imports the forms I've created
from .forms import ExerciseForm, EntryForm
#this imports the Django Login/out views
from django.contrib.auth.views import LoginView, LogoutView

from django.contrib.auth.views import UserModel
    
class UserProfileInterface(TemplateView):
    template_name = "workouts/user_profile.html"
    user = UserModel
    model = user
    context_object_name = "user"

class LogoutInterfaceView(LogoutView):
    template_name = "home/splash.html"

class LoginInterfaceView(LoginView):
    template_name = "workouts/login.html"

class ExerciseDeleteView(DeleteView):
    model = Exercises
    success_url = '/workouts/dashboard'


class ExerciseUpdateView(UpdateView):
    model = Exercises
    success_url = '/workouts/dashboard'
    form_class = ExerciseForm

class EntriesCreateView(LoginRequiredMixin, CreateView, request):
    model = Entry
    success_url = '/workouts/dashboard'
    form_class = EntryForm
    login_url = "login"
    template_name = 'workouts/entries_form.html'

    ref = request.META.get('HTTP_REFERER')
    print(ref)

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        self.object.save()
        return HttpResponseRedirect(self.get_success_url())
class ExercisesCreateView(LoginRequiredMixin, CreateView):
    model = Exercises
    success_url = '/workouts/dashboard'
    form_class = ExerciseForm
    login_url = "/login"

    #this bottom code is what gets the form Validated
    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        self.object.save()
        return HttpResponseRedirect(self.get_success_url())

class HomeView(TemplateView):
    template_name = 'workouts/welcome.html'
    extra_context = {'today': datetime.today()}

class AuthorizedView(LoginRequiredMixin, TemplateView):
    template_name = 'workouts/authorized.html'
    login_url='/admin'

class ExercisesListView(LoginRequiredMixin, ListView):
    model = Days
    context_object_name = "days"
    template_name = "workouts/exercises_list.html"
    login_url = "login"

class EntryListView(LoginRequiredMixin, ListView):
    model = Entry
    context_object_name = "entries"
    template_name = "workouts/exercise_detail.html"
    login_url = "/login"
    def get_queryset(self):
        exercise_name = self.kwargs['exercise_name']
        return self.request.user.entries.filter(exercise__name=exercise_name).order_by('-created').all

class DayListView(LoginRequiredMixin, ListView):
    model = Exercises
    context_object_name = "exercises"
    template_name = "days/sunday.html"
    login_url = "/login"


    def get_queryset(self):
        day_id = self.kwargs['day_name']
        return self.request.user.exercises.filter(days__icontains=day_id).all()