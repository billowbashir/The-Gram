# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-10-09 12:27
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0006_image_profile'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='image',
            name='profile',
        ),
    ]