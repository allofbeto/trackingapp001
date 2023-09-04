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

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'parent_category',)


admin.site.register(models.Category, CategoryAdmin)

class NumberTrackerAdmin(admin.ModelAdmin):
    list_display = ('name',)


admin.site.register(models.NumberTracker, NumberTrackerAdmin)

class TrackerEntryAdmin(admin.ModelAdmin):
    list_display = ('weight',)


admin.site.register(models.TrackerEntry, TrackerEntryAdmin)