# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-09-24 19:34
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pw_obiegi', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='handlowiec',
            old_name='name',
            new_name='handlowiec',
        ),
        migrations.RenameField(
            model_name='material',
            old_name='name',
            new_name='material',
        ),
        migrations.RenameField(
            model_name='obieg',
            old_name='name',
            new_name='obieg_name',
        ),
        migrations.RenameField(
            model_name='status',
            old_name='name',
            new_name='status',
        ),
    ]
