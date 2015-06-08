# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('downloads', '0004_remove_songs_download_count'),
    ]

    operations = [
        migrations.AddField(
            model_name='songs',
            name='download_count',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='songs',
            name='link',
            field=models.URLField(max_length=100),
        ),
    ]
