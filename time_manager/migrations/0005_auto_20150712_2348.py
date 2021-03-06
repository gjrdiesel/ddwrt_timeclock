# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('time_manager', '0004_remove_employee_hostname'),
    ]

    operations = [
        migrations.CreateModel(
            name='Hostname',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('string', models.CharField(max_length=200)),
                ('active', models.BooleanField()),
                ('employee_id', models.ForeignKey(to='time_manager.Employee')),
            ],
        ),
        migrations.RemoveField(
            model_name='hostnames',
            name='employee_id',
        ),
        migrations.DeleteModel(
            name='Hostnames',
        ),
    ]
