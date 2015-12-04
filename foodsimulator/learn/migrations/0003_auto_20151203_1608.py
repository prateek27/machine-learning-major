# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('learn', '0002_auto_20151203_1608'),
    ]

    operations = [
        migrations.RenameField(
            model_name='order',
            old_name='units_diye',
            new_name='units_delivered',
        ),
        migrations.AlterField(
            model_name='order',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2015, 12, 3, 16, 8, 53, 3786, tzinfo=utc)),
            preserve_default=True,
        ),
    ]
