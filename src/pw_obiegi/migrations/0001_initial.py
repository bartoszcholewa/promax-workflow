# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-09-24 19:05
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Handlowiec',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Material',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('producent', models.CharField(max_length=50)),
                ('dostawca', models.CharField(max_length=50)),
                ('szerokosc', models.DecimalField(decimal_places=2, max_digits=4)),
                ('dlugosc', models.DecimalField(decimal_places=2, max_digits=4)),
                ('cena', models.DecimalField(decimal_places=2, max_digits=6)),
            ],
        ),
        migrations.CreateModel(
            name='Obieg',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('kod_presta', models.CharField(max_length=50)),
                ('laminacja', models.BooleanField()),
                ('link_podgladu', models.URLField()),
                ('zamawiajacy', models.CharField(max_length=100)),
                ('data_wprowadzenia', models.DateTimeField(auto_now_add=True)),
                ('data_edycji', models.DateTimeField(auto_now=True)),
                ('handlowiec', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pw_obiegi.Handlowiec')),
                ('material', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pw_obiegi.Material')),
            ],
        ),
        migrations.CreateModel(
            name='Status',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.AddField(
            model_name='obieg',
            name='status',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pw_obiegi.Status'),
        ),
    ]