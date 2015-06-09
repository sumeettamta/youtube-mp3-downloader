# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('downloads', '0010_auto_20150605_0850'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userhistory',
            name='song',
        ),
        migrations.DeleteModel(
            name='UserHistory',
        ),
    ]
