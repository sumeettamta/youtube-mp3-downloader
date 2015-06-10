# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('downloads', '0006_auto_20150604_2018'),
    ]

    operations = [
        migrations.AlterField(
            model_name='songs',
            name='like_count',
            field=models.PositiveIntegerField(default=0, null=True),
        ),
    ]
