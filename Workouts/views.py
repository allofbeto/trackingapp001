from datetime import datetime
from django.http.response import HttpResponseRedirect
from django.template.context_processors import request

#this imports the models I've created
from .models import Exercises,Entry, Days, Category
#this allows me to create/edit/delete model entries
from django.views.generic import CreateView, UpdateView, TemplateView, ListView, DetailView
from django.views.generic.edit import DeleteView
#this allows me to password protect pages
from django.contrib.auth.mixins import LoginRequiredMixin
#This imports the forms I've created
from .forms import ExerciseForm, EntryForm, CategoryForm
#this imports the Django Login/out views
from django.contrib.auth.views import LoginView, LogoutView

from django.contrib.auth.views import UserModel
from django.urls import reverse_lazy, resolve
from django.urls import reverse

from django.shortcuts import render, redirect
from .models import Category, NumberTracker
from django.views import View

    
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

class EntriesCreateView(LoginRequiredMixin, CreateView):
    model = Entry
    success_url = '/workouts/dashboard'
    form_class = EntryForm
    login_url = "login"
    template_name = 'workouts/entries_form.html'

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
    template_name = 'workouts/exercises_form.html'

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


class EntryListView(LoginRequiredMixin, CreateView, ListView, HttpResponseRedirect):
    model = Entry
    context_object_name = "entries"
    template_name = "workouts/exercise_detail.html"
    login_url = "/login"
    form_class = EntryForm

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs["eid"] = self.kwargs['exercise_id']
        return kwargs

    def get_success_url(self):
        return self.request.path
    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        self.object.save()
        return HttpResponseRedirect(self.get_success_url())
    def get_queryset(self):
        exercise_id = self.kwargs['exercise_id']
        return self.request.user.entries.filter(exercise__id=exercise_id).order_by('-created').all

class DayListView(LoginRequiredMixin, CreateView, ListView):
    model = Exercises
    context_object_name = "exercises"
    template_name = "days/sunday.html"
    login_url = "/login"
    form_class = ExerciseForm

    def get_success_url(self):
        return self.request.path
    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        self.object.save()
        return HttpResponseRedirect(self.get_success_url())


    def get_queryset(self):
        day_id = self.kwargs['day_name']
        return self.request.user.exercises.filter(days__icontains=day_id).all

    def get_day_list_url(self):
        # Replace 'day-list-url-name' with the name of the URL pattern for the DayListView
        day_list_url = reverse('day-list')
        return day_list_url

class NewExerciseListView(LoginRequiredMixin, CreateView, ListView):
    model = Exercises
    context_object_name = "exercises"
    template_name = "workouts/new_exercise_list_display.html"
    login_url = "/login"
    form_class = ExerciseForm

    def get_success_url(self):
        return self.request.path
    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        self.object.save()
        return HttpResponseRedirect(self.get_success_url())

class NewExerciseEnryListDisplay(LoginRequiredMixin, CreateView, ListView, HttpResponseRedirect):
    model = Entry
    context_object_name = "entries"
    template_name = "workouts/exercise_detail.html"
    login_url = "/login"
    form_class = EntryForm

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs["eid"] = self.kwargs['exercise_id']
        return kwargs

    def get_success_url(self):
        return self.request.path
    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        self.object.save()
        return HttpResponseRedirect(self.get_success_url())
    def get_queryset(self):
        exercise_id = self.kwargs['exercise_id']
        return self.request.user.entries.filter(exercise__id=exercise_id).order_by('-created').all

class NewDisplayEntriesCreateView(LoginRequiredMixin, CreateView):
    model = Entry
    success_url = '/workouts/dashboard'
    form_class = EntryForm
    login_url = "login"
    template_name = 'workouts/new_display_entry_form.html'

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        self.object.save()
        return HttpResponseRedirect(self.get_success_url())


def create_category(request):
    categories = Category.objects.filter(parent_category__isnull=True)

    if request.method == 'POST':
        form = CategoryForm(request.POST)
        if form.is_valid():
            category = form.save()  # Save the new category to the database

            # Use the reverse function to generate the URL
            add_child_or_tracker_url = reverse('workouts:add_child_or_tracker', args=[category.id])

            return redirect(add_child_or_tracker_url)  # Redirect to the generated URL
    else:
        form = CategoryForm()

    return render(request, 'workouts/create_category.html', {'form': form, 'categories': categories})


def add_child_or_tracker(request, category_id):
    category = Category.objects.get(id=category_id)
    trackers = NumberTracker.objects.filter(category=category)

    if request.method == 'POST':
        form = CategoryForm(request.POST)
        if form.is_valid():
            new_category = form.save(commit=False)
            new_category.parent_category = category
            new_category.save()

            # Use the reverse function to generate the URL
            add_child_or_tracker_url = reverse('workouts:add_child_or_tracker', args=[category.id])

            return redirect(add_child_or_tracker_url)  # Redirect to the generated URL
    else:
        initial_data = {'parent_category': category.id}  # Set initial data for the "Parent Category" field
        form = CategoryForm(initial=initial_data)  # Pass the initial data to the form

    return render(request, 'workouts/add_child_or_tracker.html', {'form': form, 'category': category, 'trackers': trackers})

class NewExerciseListView(View):
    template_name = 'workouts/new_display_entry_form.html'

    def get(self, request, category_id, tracker_id):
        category = Category.objects.get(id=category_id)
        tracker = NumberTracker.objects.get(id=tracker_id)

        return render(request, self.template_name, {'category': category, 'tracker': tracker})
