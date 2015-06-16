# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0002_auto_20150616_0823'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cartitem',
            name='song',
            field=models.ForeignKey(to='downloads.Songs'),
        ),
    ]
