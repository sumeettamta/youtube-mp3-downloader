# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('downloads', '0003_auto_20150604_0650'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='songs',
            name='download_count',
        ),
    ]
