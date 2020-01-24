# -*- coding: utf-8 -*-
# Generated by Django 1.11.17 on 2020-01-13 23:48
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('bug', '0005_auto_20200111_1938'),
    ]

    operations = [
        migrations.AddField(
            model_name='bug',
            name='done',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='comment',
            name='bug',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='bug.Bug'),
        ),
    ]