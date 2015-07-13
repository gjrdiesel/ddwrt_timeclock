# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('time_manager', '0003_hostnames'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='employee',
            name='hostname',
        ),
    ]
