from django.urls import path
from . import views
from Workouts.views import ExercisesListView

urlpatterns = [
    path('home', views.HomeView.as_view(), name='home'),
    path('authorized', views.AuthorizedView.as_view(), name='authorized'),
    path('dashboard', views.ExercisesListView.as_view(), name='dashboard'),
    path('details/<int:exercise_id>', views.EntryListView.as_view(), name='details'),
    path('delete-exercise/<int:pk>', views.ExerciseDeleteView.as_view(), name='delete-exercise'),
    path('edit-exercise/<int:pk>', views.ExerciseUpdateView.as_view(), name='edit-exercise'),
    path('entry/new', views.EntriesCreateView.as_view(), name="entry_new"),
    path('exercise/new', views.ExercisesCreateView.as_view(), name="exercise.new"),
    path('login', views.LoginInterfaceView.as_view(), name="login"),
    path('logout', views.LogoutInterfaceView.as_view(), name="logout"),
    path('day/<str:day_name>', views.DayListView.as_view(), name= "day"),
    path('user-profile', views.UserProfileInterface.as_view(), name='user-profile')
]