from django.contrib import admin

from . import models


class DaysAdmin(admin.ModelAdmin):
    list_display = ('name',)

admin.site.register(models.Days, DaysAdmin)

class ExercisesAdmin(admin.ModelAdmin):
    list_display = ('name',)



admin.site.register(models.Exercises, ExercisesAdmin)

class EntryAdmin(admin.ModelAdmin):
    list_display = ('created',)


admin.site.register(models.Entry, EntryAdmin)

class Entry2Admin(admin.ModelAdmin):
    list_display = ('created',)


admin.site.register(models.Entry2, EntryAdmin)