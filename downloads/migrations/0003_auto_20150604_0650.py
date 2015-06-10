# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('downloads', '0002_auto_20150603_1054'),
    ]

    operations = [
        migrations.RenameField(
            model_name='userhistory',
            old_name='download_dt',
            new_name='datetime',
        ),
        migrations.RenameField(
            model_name='userhistory',
            old_name='song_id',
            new_name='song',
        ),
        migrations.RemoveField(
            model_name='songs',
            name='song_id',
        ),
    ]
