# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('tournament', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='game',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2015, 5, 25, 15, 12, 55, 749729, tzinfo=utc), verbose_name=b'Date', blank=True),
            preserve_default=False,
        ),
    ]
