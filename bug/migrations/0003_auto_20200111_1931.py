# -*- coding: utf-8 -*-
# Generated by Django 1.11.17 on 2020-01-11 19:31
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('bug', '0002_auto_20200110_1950'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='bug',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='bug.Bug'),
        ),
    ]
