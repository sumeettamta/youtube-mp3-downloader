# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import User.manager


class Migration(migrations.Migration):

    dependencies = [
        ('User', '0002_user_is_active'),
    ]

    operations = [
        migrations.AlterModelManagers(
            name='user',
            managers=[
                ('objects', User.manager.CustomUserManager()),
            ],
        ),
        migrations.AddField(
            model_name='user',
            name='is_staff',
            field=models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status'),
        ),
    ]
