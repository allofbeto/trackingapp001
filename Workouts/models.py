from django.db import models
from django.contrib.auth.models import User

from multiselectfield import  MultiSelectField

UNITS = (
    ('lbs', 'LBS'),
    ('kg', 'KG'),
)

DAYS = (
    ('SUN', 'sun'),
    ('MON', 'mon'),
    ('TUE', 'tue'),
    ('WED', 'wed'),
    ('THU', 'thu'),
    ('FRI', 'fri'),
    ('SAT', 'sat'),
)


class Days(models.Model):
    name = models.CharField(max_length=3, choices=DAYS)
    icon_url = models.TextField()

class Exercises(models.Model):
    name = models.CharField(max_length=100)
    units = models.CharField(max_length=3, choices=UNITS)
    days = MultiSelectField(choices=DAYS)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='exercises')

    def __str__(self):
        return self.name


class Entry(models.Model):
    exercise = models.ForeignKey(
        'Exercises',
        on_delete= models.CASCADE,
    )
    weight = models.DecimalField(max_digits=6, decimal_places=2)
    notes = models.TextField(blank=True)
    reps = models.IntegerField()
    created = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='entries')

class Entry2(models.Model):
    exercise = models.ManyToManyField(Exercises)
    weight = models.DecimalField(max_digits=6, decimal_places=2)
    notes = models.TextField(blank=True)
    reps = models.IntegerField()
    created = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='entries2')


from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=100)
    parent_category = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.name


class NumberTracker(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    number = models.IntegerField()

    def __str__(self):
        return f"{self.category.name} - {self.number}"