# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2016-11-10 17:31
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bot', '0006_auto_20161103_2312'),
    ]

    operations = [
        migrations.RenameField(
            model_name='groupmebot',
            old_name='botid',
            new_name='botID',
        ),
        migrations.AddField(
            model_name='groupmebot',
            name='victimID',
            field=models.IntegerField(default=0, unique=True),
        ),
    ]