# Generated by Django 2.0 on 2018-09-07 01:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0004_set_session'),
    ]

    operations = [
        migrations.AddField(
            model_name='exercise',
            name='muscle_groups',
            field=models.ManyToManyField(to='api.MuscleGroup'),
        ),
    ]
