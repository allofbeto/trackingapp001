# Generated by Django 3.2.7 on 2023-08-27 17:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Workouts', '0020_remove_exercises_category'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='category',
            name='reps',
        ),
        migrations.RemoveField(
            model_name='category',
            name='units',
        ),
    ]