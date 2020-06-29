# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('django_cron', '0002_auto_20161118_1325'),
    ]

    operations = [
        migrations.AlterField(
            model_name='job',
            name='instance',
            field=models.BinaryField(max_length=None),
        ),
        migrations.AlterField(
            model_name='job',
            name='args',
            field=models.BinaryField(max_length=None),
        ),
        migrations.AlterField(
            model_name='job',
            name='kwargs',
            field=models.BinaryField(max_length=None),
        ),
    ]
