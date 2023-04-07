from django.urls import path
from . import views

urlpatterns = [
    path('home', views.HomeView.as_view(), name='home'),
    path('authorized', views.AuthorizedView.as_view(), name='authorized'),
    path('dashboard', views.ExercisesListView.as_view(), name='dashboard'),
    path('details/<int:pk>', views.ExerciseDetailView.as_view(), name='details'),
    path('entry/<int:pk>', views.EntryDetailView.as_view()),
]