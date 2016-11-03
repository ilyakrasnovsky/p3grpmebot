# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2016-11-03 21:07
from __future__ import unicode_literals

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bot', '0004_auto_20161103_2105'),
    ]

    operations = [
        migrations.AlterField(
            model_name='groupmebot',
            name='avatar_url',
            field=models.URLField(default='www.google.com', validators=[django.core.validators.URLValidator]),
        ),
        migrations.AlterField(
            model_name='groupmebot',
            name='callback_url',
            field=models.URLField(default='www.google.com', validators=[django.core.validators.URLValidator]),
        ),
    ]
