from django.db import models
from django.contrib.auth.models import User


from multiselectfield import  MultiSelectField
from django.contrib.auth import get_user

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


class Category(models.Model):
   name = models.CharField(max_length=100)
   parent_category = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True)
   user = models.ForeignKey(User, on_delete=models.CASCADE)

   def __str__(self):
      return self.name


class NumberTracker(models.Model):
   name = models.CharField(max_length=100)
   category = models.ForeignKey(Category, on_delete=models.CASCADE)
   units = models.CharField(max_length=3, choices=UNITS)
   user = models.ForeignKey(User, on_delete=models.CASCADE)

   def __str__(self):
      return self.name


class TrackerEntry(models.Model):
   weight = models.FloatField()
   rep = models.IntegerField()
   note = models.CharField(max_length=1000)
   user = models.ForeignKey(User, on_delete=models.CASCADE)
   nothing = models.TextField(max_length=100, blank=True)
   number_tracker = models.ForeignKey(NumberTracker, on_delete=models.CASCADE)
   created = models.DateTimeField(auto_now_add=True)


