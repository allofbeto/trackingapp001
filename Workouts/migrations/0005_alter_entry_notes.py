# Generated by Django 3.2.7 on 2023-04-20 23:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Workouts', '0004_alter_entry_reps'),
    ]

    operations = [
        migrations.AlterField(
            model_name='entry',
            name='notes',
            field=models.TextField(null=True),
        ),
    ]
