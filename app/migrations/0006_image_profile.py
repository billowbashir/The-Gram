# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-10-09 11:33
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_profile'),
    ]

    operations = [
        migrations.AddField(
            model_name='image',
            name='profile',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='app.Profile'),
        ),
    ]
