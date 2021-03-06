# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-27 21:34
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('retake', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Poke',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('numberPokes', models.IntegerField()),
                ('createdat', models.DateTimeField(auto_now_add=True)),
                ('updatedat', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.AddField(
            model_name='user',
            name='poke_count',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='poke',
            name='got_poked',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='poke_get', to='retake.User'),
        ),
        migrations.AddField(
            model_name='poke',
            name='poked_by',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='poke_give', to='retake.User'),
        ),
    ]
