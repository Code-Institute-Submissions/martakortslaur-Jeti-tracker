# -*- coding: utf-8 -*-
# Generated by Django 1.11.17 on 2020-01-13 23:48
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('checkout', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='orderlineitem',
            name='feature',
        ),
        migrations.RemoveField(
            model_name='orderlineitem',
            name='order',
        ),
        migrations.DeleteModel(
            name='Order',
        ),
        migrations.DeleteModel(
            name='OrderLineItem',
        ),
    ]