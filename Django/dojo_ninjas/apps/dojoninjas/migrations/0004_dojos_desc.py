# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-17 17:24
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dojoninjas', '0003_auto_20171017_0824'),
    ]

    operations = [
        migrations.AddField(
            model_name='dojos',
            name='desc',
            field=models.TextField(null=True),
        ),
    ]
