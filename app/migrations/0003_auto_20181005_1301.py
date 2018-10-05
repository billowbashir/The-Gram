# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-10-05 13:01
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_auto_20181005_1254'),
    ]

    operations = [
        migrations.CreateModel(
            name='like',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('like', models.IntegerField()),
            ],
        ),
        migrations.AlterField(
            model_name='image',
            name='likes',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.like'),
        ),
    ]
