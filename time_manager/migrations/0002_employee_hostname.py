# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('time_manager', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='employee',
            name='hostname',
            field=models.CharField(default='unknown', max_length=200),
            preserve_default=False,
        ),
    ]
