# Generated by Django 3.2.7 on 2023-05-02 18:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Workouts', '0007_days'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Days',
            new_name='Day',
        ),
    ]
