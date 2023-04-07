from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime
from .models import Exercises,Entry
from django.http import Http404
from django.views.generic import TemplateView, ListView, DetailView
from django.contrib.auth.mixins import LoginRequiredMixin

class HomeView(TemplateView):
    template_name = 'workouts/welcome.html'
    extra_context = {'today': datetime.today()}

class AuthorizedView(LoginRequiredMixin, TemplateView):
    template_name = 'workouts/authorized.html'
    login_url='/admin'

class ExercisesListView(ListView):
    model = Exercises
    model_2 = Entry
    context_object_name = "exercises"
    context_object_name_2 = "entries"
    template_name = "workouts/exercises_list.html"

class ExerciseDetailView(DetailView):
    model = Entry
    context_object_name = "entry"
    template_name = "workouts/exercise_detail.html"

class EntryDetailView(DetailView):
    model = Entry
    context_object_name = "entry"
    template_name = "workouts/welcome"