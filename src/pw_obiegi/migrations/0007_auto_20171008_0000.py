# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-08 00:00
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pw_obiegi', '0006_auto_20171007_2344'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='obieg',
            name='obieg_category',
        ),
        migrations.AddField(
            model_name='obieg',
            name='obieg_type',
            field=models.BooleanField(default=False),
        ),
    ]