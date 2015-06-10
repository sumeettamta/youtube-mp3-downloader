# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Songs',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('link', models.URLField(unique=True, max_length=100)),
                ('title', models.CharField(default=b'', max_length=200)),
                ('uploader', models.CharField(default=b'', max_length=30)),
                ('view_count', models.PositiveIntegerField()),
                ('like_count', models.PositiveIntegerField()),
                ('unlike_count', models.PositiveIntegerField()),
                ('download_count', models.PositiveIntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='UserHistory',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('download_dt', models.DateTimeField()),
                ('song_id', models.ForeignKey(to='downloads.Songs')),
            ],
        ),
        migrations.AddField(
            model_name='songs',
            name='song_id',
            field=models.ForeignKey(to='downloads.UserHistory'),
        ),
    ]
