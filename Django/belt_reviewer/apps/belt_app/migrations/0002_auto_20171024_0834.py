# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-24 13:34
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('belt_app', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='alias',
            new_name='lastname',
        ),
    ]
