# Generated by Django 3.2.7 on 2023-08-27 17:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Workouts', '0018_auto_20230827_1719'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='reps',
            field=models.IntegerField(blank=True),
        ),
        migrations.AlterField(
            model_name='category',
            name='units',
            field=models.CharField(blank=True, max_length=10),
        ),
    ]
