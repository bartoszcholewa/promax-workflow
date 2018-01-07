# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-18 21:33
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pw_obiegi', '0008_obieg_uwagi'),
    ]

    operations = [
        migrations.AlterField(
            model_name='obieg',
            name='handlowiec',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.DeleteModel(
            name='Handlowiec',
        ),
    ]