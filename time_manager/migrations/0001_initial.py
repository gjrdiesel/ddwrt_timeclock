# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='StateChange',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('state', models.BooleanField()),
                ('time', models.DateTimeField(auto_now=True)),
                ('employee_id', models.ForeignKey(to='time_manager.Employee')),
            ],
        ),
        migrations.CreateModel(
            name='TimePeriod',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('day', models.DateField(verbose_name=b'day')),
                ('clock_in', models.DateTimeField(verbose_name=b'time in')),
                ('clock_out', models.DateTimeField(verbose_name=b'time out')),
                ('hours', models.IntegerField()),
                ('overtime', models.IntegerField()),
                ('employee', models.ForeignKey(to='time_manager.Employee')),
            ],
        ),
    ]
