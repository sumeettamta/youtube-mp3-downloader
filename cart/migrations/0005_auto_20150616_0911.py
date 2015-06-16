# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('downloads', '__first__'),
        ('cart', '0004_auto_20150616_0910'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cartitem',
            name='song',
        ),
        migrations.AddField(
            model_name='cartitem',
            name='song',
            field=models.ForeignKey(to='downloads.Songs', null=True),
        ),
    ]
