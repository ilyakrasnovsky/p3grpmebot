# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2016-11-03 23:12
from __future__ import unicode_literals

import django.core.validators
from django.db import migrations, models
import django.db.models.manager


class Migration(migrations.Migration):

    dependencies = [
        ('bot', '0005_auto_20161103_2107'),
    ]

    operations = [
        migrations.AlterModelManagers(
            name='groupmebot',
            managers=[
                ('botmanager', django.db.models.manager.Manager()),
            ],
        ),
        migrations.AddField(
            model_name='groupmebot',
            name='groupname',
            field=models.TextField(default='Tests'),
        ),
        migrations.AlterField(
            model_name='groupmebot',
            name='avatar_url',
            field=models.URLField(default='https://www.google.com', validators=[django.core.validators.URLValidator]),
        ),
        migrations.AlterField(
            model_name='groupmebot',
            name='callback_url',
            field=models.URLField(default='https://www.google.com', validators=[django.core.validators.URLValidator]),
        ),
    ]
