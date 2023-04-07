from django.db import models

UNITS = (
    ('lbs', 'LBS'),
    ('kg', 'KG'),
)

class Exercises(models.Model):
    name = models.CharField(max_length=100)
    units = models.CharField(max_length=3, choices=UNITS)

    def __str__(self):
        return self.name


class Entry(models.Model):
    exercise = models.ForeignKey(
        'Exercises',
        on_delete= models.CASCADE,
    )
    weight = models.DecimalField(max_digits=6, decimal_places=2)
    notes = models.TextField(blank=True)
    created = models.DateTimeField(auto_now_add=True)