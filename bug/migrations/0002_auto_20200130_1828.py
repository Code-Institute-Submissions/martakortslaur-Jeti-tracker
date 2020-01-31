# -*- coding: utf-8 -*-
# Generated by Django 1.11.27 on 2020-01-30 18:28
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('bug', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='bug',
            name='posted_on',
            field=models.DateTimeField(blank=True, default=django.utils.timezone.now, null=True),
        ),
        migrations.AddField(
            model_name='comment',
            name='created_on',
            field=models.DateTimeField(blank=True, default=django.utils.timezone.now, null=True),
        ),
    ]