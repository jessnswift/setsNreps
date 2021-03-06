# Generated by Django 2.0 on 2018-09-13 01:43

from django.db import migrations, models
import django.utils.datetime_safe


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0012_auto_20180912_0336'),
    ]

    operations = [
        migrations.AddField(
            model_name='session',
            name='date_completed',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='session',
            name='date_created',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.datetime_safe.datetime.utcnow),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='set',
            name='date_completed',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='set',
            name='date_created',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.datetime_safe.datetime.utcnow),
            preserve_default=False,
        ),
    ]
