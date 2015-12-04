# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('learn', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='units_delievered',
        ),
        migrations.AddField(
            model_name='order',
            name='units_diye',
            field=models.IntegerField(default=0),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='order',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2015, 12, 3, 16, 8, 18, 159451, tzinfo=utc)),
            preserve_default=True,
        ),
    ]
