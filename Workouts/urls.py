from django.urls import path
from . import views
from Workouts.views import ExercisesListView


app_name = 'workouts'


urlpatterns = [
   path('home', views.HomeView.as_view(), name='home'),
   path('authorized', views.AuthorizedView.as_view(), name='authorized'),
   path('dashboard', views.ExercisesListView.as_view(), name='dashboard'),
   path('details/<int:exercise_id>', views.EntryListView.as_view(), name='details'),
   path('delete-exercise/<int:pk>', views.ExerciseDeleteView.as_view(), name='delete-exercise'),
   path('edit-exercise/<int:pk>', views.ExerciseUpdateView.as_view(), name='edit-exercise'),
   path('entry/new', views.EntriesCreateView.as_view(), name="entry_new"),
   path('exercise/new', views.ExercisesCreateView.as_view(), name="exercise_new"),
   path('login', views.LoginInterfaceView.as_view(), name="login"),
   path('logout', views.LogoutInterfaceView.as_view(), name="logout"),
   path('new_display_entry_form', views.NewDisplayEntriesCreateView.as_view(), name="new_entry_display"),
   path('new_entry_list_display/<int:exercise_id>', views.NewExerciseEnryListDisplay.as_view(), name="new_exercise_entry_list"),
   path('day/<str:day_name>', views.DayListView.as_view(), name= "day"),
   path('user-profile', views.UserProfileInterface.as_view(), name='user-profile'),


   path('create-category/', views.create_category, name='create_category'),
   path('add-child-or-tracker/<int:category_id>/', views.add_child_or_tracker, name='add_child_or_tracker'),
   path('new_exercise_list/<int:category_id>/<int:tracker_id>/', views.NewExerciseListView.as_view(), name="new_exercise_list"),
]
