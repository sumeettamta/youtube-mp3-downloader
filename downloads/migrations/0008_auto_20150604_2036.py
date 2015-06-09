# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('downloads', '0007_auto_20150604_2035'),
    ]

    operations = [
        migrations.AlterField(
            model_name='songs',
            name='download_count',
            field=models.PositiveIntegerField(default=0, null=True),
        ),
        migrations.AlterField(
            model_name='songs',
            name='unlike_count',
            field=models.PositiveIntegerField(default=0, null=True),
        ),
        migrations.AlterField(
            model_name='songs',
            name='view_count',
            field=models.PositiveIntegerField(default=0, null=True),
        ),
    ]
