# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-07 23:32
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pw_obiegi', '0004_obieg_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='obieg',
            name='obieg_category',
            field=models.CharField(default='normalny', max_length=50),
        ),
    ]
