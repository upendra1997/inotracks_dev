# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2017-07-02 19:16
from __future__ import unicode_literals

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Bus',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bus_number', models.CharField(max_length=100)),
                ('running_status', models.BooleanField(default=True)),
                ('shifts', models.IntegerField(default=0)),
                ('driver', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='users.InoDriver')),
            ],
            options={
                'verbose_name_plural': 'Buses',
                'verbose_name': 'Bus',
            },
        ),
        migrations.CreateModel(
            name='BusParameter',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bus_number', models.CharField(max_length=100)),
                ('speed', models.IntegerField()),
                ('fuel', models.IntegerField()),
                ('distance', models.IntegerField()),
                ('time_recorded', models.DateTimeField(default=datetime.datetime.now)),
            ],
        ),
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('latitude', models.FloatField(blank=True, null=True)),
                ('longitude', models.FloatField(blank=True, null=True)),
                ('place_name', models.TextField(blank=True, null=True)),
                ('known_location', models.BooleanField(default=False)),
                ('time_recorded', models.DateTimeField(default=datetime.datetime.now)),
            ],
        ),
        migrations.CreateModel(
            name='Stop',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('arrival_time', models.DateTimeField()),
                ('departure_time', models.DateTimeField()),
                ('halt_time', models.DurationField(blank=True, null=True)),
                ('location', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Buses.Location')),
            ],
        ),
        migrations.CreateModel(
            name='TimeTable',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bus', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='Buses.Bus')),
                ('stoppage', models.ManyToManyField(to='Buses.Stop')),
            ],
        ),
        migrations.AddField(
            model_name='bus',
            name='location',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='Buses.Location'),
        ),
        migrations.AddField(
            model_name='bus',
            name='owner',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='bus',
            name='parameters',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='Buses.BusParameter'),
        ),
    ]