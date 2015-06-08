# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('downloads', '0009_auto_20150604_2050'),
    ]

    operations = [
        migrations.RenameField(
            model_name='songs',
            old_name='link',
            new_name='youtube_link',
        ),
        migrations.AddField(
            model_name='songs',
            name='local_link',
            field=models.URLField(default=b'', max_length=300),
        ),
    ]
