# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-10-22 17:21
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('loginregis_app', '0009_auto_20171022_1619'),
    ]

    operations = [
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('item_name', models.CharField(max_length=255)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('listed_by', models.ManyToManyField(related_name='listed_items', to='loginregis_app.User')),
                ('uploader', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='uploaded_items', to='loginregis_app.User')),
            ],
        ),
    ]
