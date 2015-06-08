# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('downloads', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='songs',
            name='download_count',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='songs',
            name='like_count',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='songs',
            name='unlike_count',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='songs',
            name='uploader',
            field=models.CharField(default=b'', max_length=30, blank=True),
        ),
        migrations.AlterField(
            model_name='songs',
            name='view_count',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='userhistory',
            name='download_dt',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
