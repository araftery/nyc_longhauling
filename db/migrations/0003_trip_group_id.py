# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-04-29 16:21
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('db', '0002_auto_20160429_1347'),
    ]

    operations = [
        migrations.AddField(
            model_name='trip',
            name='group_id',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
