# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('downloads', '__first__'),
        ('cart', '0003_auto_20150616_0907'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cartitem',
            name='song',
        ),
        migrations.AddField(
            model_name='cartitem',
            name='song',
            field=models.ManyToManyField(to='downloads.Songs'),
        ),
    ]
