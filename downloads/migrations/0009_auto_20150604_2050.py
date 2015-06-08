# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('downloads', '0008_auto_20150604_2036'),
    ]

    operations = [
        migrations.AlterField(
            model_name='songs',
            name='link',
            field=models.URLField(unique=True, max_length=100),
        ),
    ]
