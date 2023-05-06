from django.db import models
from django.contrib.auth.models import User

UNITS = (
    ('lbs', 'LBS'),
    ('kg', 'KG'),
)

DAYS = (
    ('SUN', 'SUN'),
    ('MON', 'MON'),
    ('TUE', 'TUE'),
    ('WED', 'WED'),
    ('THU', 'THU'),
    ('FRI', 'FRI'),
    ('SAT', 'SAT'),
)


class Exercises(models.Model):
    name = models.CharField(max_length=100)
    units = models.CharField(max_length=3, choices=UNITS)
    days = models.CharField(max_length=3, choices=DAYS)
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