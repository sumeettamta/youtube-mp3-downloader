# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('downloads', '0005_auto_20150604_2016'),
    ]

    operations = [
        migrations.AlterField(
            model_name='songs',
            name='uploader',
            field=models.CharField(default=b'', max_length=50, blank=True),
        ),
    ]
