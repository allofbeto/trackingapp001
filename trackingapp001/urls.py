from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.contrib.staticfiles.urls import staticfiles_urlpatterns


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('home.urls')),
    path('workouts/', include('Workouts.urls')),
]
#
urlpatterns += staticfiles_urlpatterns()

