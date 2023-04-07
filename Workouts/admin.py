from django.contrib import admin

from . import models

class ExercisesAdmin(admin.ModelAdmin):
    list_display = ('name',)

admin.site.register(models.Exercises, ExercisesAdmin)

class EntryAdmin(admin.ModelAdmin):
    list_display = ("exercise", 'created',)

admin.site.register(models.Entry, EntryAdmin)