# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-07-26 19:29
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('belt_exam_app', '0002_trip_guest'),
    ]

    operations = [
        migrations.AlterField(
            model_name='trip',
            name='guest',
            field=models.ManyToManyField(related_name='trip_guests', to='login_app.User'),
        ),
    ]
