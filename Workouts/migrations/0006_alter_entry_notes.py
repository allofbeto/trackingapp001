# Generated by Django 3.2.7 on 2023-04-21 00:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Workouts', '0005_alter_entry_notes'),
    ]

    operations = [
        migrations.AlterField(
            model_name='entry',
            name='notes',
            field=models.TextField(blank=True, default=1),
            preserve_default=False,
        ),
    ]
