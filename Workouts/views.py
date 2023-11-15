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
from .forms import ExerciseForm, EntryForm, CategoryForm, NumberTrackerForm, TrackerEntryForm, TrackerEntry
#this imports the Django Login/out views
from django.contrib.auth.views import LoginView, LogoutView


from django.contrib.auth.views import UserModel
from django.urls import reverse_lazy, resolve
from django.urls import reverse


from django.shortcuts import render, redirect, get_object_or_404
from .models import Category, NumberTracker
from django.views import View
from django.contrib.auth import get_user


# Define the get_current_user function to access the authenticated user
def get_current_user(request):
    return get_user(request)

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



#as of 09.02.2023 9:36 views tie authenticated user to the created models below and filters them out
class CreateCategoryView(LoginRequiredMixin, View):
    login_url = '/login/'  # The URL to redirect to if the user is not logged in
    redirect_field_name = 'next'  # The query parameter to store the original URL

    def get(self, request):
        categories = Category.objects.filter(user=request.user, parent_category__isnull=True)
        category_form = CategoryForm(prefix='category')
        tracker_form = NumberTrackerForm(prefix='tracker')
        return render(request, 'workouts/create_category.html', {'category_form': category_form, 'tracker_form': tracker_form, 'categories': categories})

    def post(self, request):
        category_form = CategoryForm(request.POST, prefix='category')
        tracker_form = NumberTrackerForm(request.POST, prefix='tracker')

        if category_form.is_valid() and 'create_category' in request.POST:
            category = category_form.save(commit=False)
            category.user = request.user
            category.save()
            add_child_or_tracker_url = reverse('workouts:add_child_or_tracker', args=[category.id])
            return redirect(add_child_or_tracker_url)

        elif tracker_form.is_valid() and 'create_tracker' in request.POST:
            tracker = tracker_form.save(commit=False)
            tracker.user = request.user
            tracker.save()
            add_child_or_tracker_url = reverse('workouts:add_child_or_tracker', args=[tracker.category.id])
            return redirect(add_child_or_tracker_url)

        categories = Category.objects.filter(user=request.user, parent_category__isnull=True)
        return render(request, 'workouts/create_category.html', {'category_form': category_form, 'tracker_form': tracker_form, 'categories': categories})

class AddChildOrTrackerView(LoginRequiredMixin, View):
    login_url = '/login/'  # The URL to redirect to if the user is not logged in
    redirect_field_name = 'next'  # The query parameter to store the original URL

    def get(self, request, category_id):
        parent_category = get_object_or_404(Category, id=category_id, user=request.user)
        categories = Category.objects.filter(user=request.user, parent_category=parent_category)
        trackers = NumberTracker.objects.filter(user=request.user, category=parent_category).order_by('name')
        category_form = CategoryForm(initial={'parent_category': parent_category}, prefix='category')
        tracker_form = NumberTrackerForm(initial={'category': parent_category}, prefix='tracker')
        entry_form = TrackerEntryForm()
        return render(request, 'workouts/add_child_or_tracker.html', {'entry_form':entry_form, 'category_form': category_form, 'tracker_form': tracker_form, 'categories': categories, 'trackers': trackers, 'parent_category': parent_category})

    def post(self, request, category_id):
        parent_category = get_object_or_404(Category, id=category_id)
        categories = Category.objects.filter(parent_category=parent_category)
        trackers = NumberTracker.objects.filter(category=parent_category)
        category_form = CategoryForm(request.POST, prefix='category')
        tracker_form = NumberTrackerForm(request.POST, prefix='tracker')
        tracker = NumberTracker()
        number_tracker = tracker.name
        entry_form = TrackerEntryForm(request.POST)
        #Inputs submitt properly
        if entry_form.is_valid():
            entry = entry_form.save(commit=False)
            entry.user = request.user
            entry.save()

        if category_form.is_valid() and 'create_category' in request.POST:
            category = category_form.save(commit=False)
            category.user = request.user  # Set the user field
            category.parent_category = parent_category
            category.save()
            add_child_or_tracker_url = reverse('workouts:add_child_or_tracker', args=[category.id])
            return redirect(add_child_or_tracker_url)

        elif tracker_form.is_valid() and 'create_tracker' in request.POST:
            tracker = tracker_form.save(commit=False)
            tracker.user = request.user  # Set the user field
            tracker.category = parent_category
            tracker.save()
            return redirect('workouts:new_exercise_list', category_id=parent_category.id, tracker_id=tracker.id)

        return render(request, 'workouts/add_child_or_tracker.html', {'entry_form':entry_form, 'category_form': category_form, 'tracker_form': tracker_form, 'categories': categories, 'trackers': trackers, 'parent_category': parent_category})

class NewExerciseListView(View):
    template_name = 'workouts/new_display_entry_form.html'

    def get(self, request, category_id, tracker_id):
        category = get_object_or_404(Category, id=category_id)
        tracker = get_object_or_404(NumberTracker, id=tracker_id)
        form = TrackerEntryForm(initial={'number_tracker': tracker})
        tracker_entries = TrackerEntry.objects.filter(number_tracker=tracker).order_by('-created')
        return render(request, self.template_name, {'category': category, 'tracker': tracker, 'form': form, 'tracker_entries': tracker_entries,})

    def post(self, request, category_id, tracker_id):
        category = get_object_or_404(Category, id=category_id)
        tracker = get_object_or_404(NumberTracker, id=tracker_id)

        if 'create_entry' in request.POST:
            form = TrackerEntryForm(request.POST)
            if form.is_valid():
                entry = form.save(commit=False)
                entry.user = request.user
                entry.number_tracker = tracker
                entry.save()

                # Create a new empty form and set focus to the first field
                form = TrackerEntryForm()
                form.fields['weight'].widget.attrs['autofocus'] = True  # Auto-select 'weight' field

                # Redirect to the same page to clear the URL and avoid resubmission
                return HttpResponseRedirect(request.path_info)
        else:
            form = TrackerEntryForm()

            return render(request, self.template_name, {'category': category, 'tracker': tracker, 'form': form})
        return render(request, self.template_name, {'category': category, 'tracker': tracker, 'form': form})
    # tracker entry form and filter is working Perfectly


