# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('learn', '0006_auto_20151203_1626'),
    ]

    operations = [
        migrations.CreateModel(
            name='result',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('students', models.IntegerField(default=45)),
                ('lr', models.IntegerField(default=45)),
                ('rr', models.IntegerField(default=45)),
                ('svm', models.IntegerField(default=45)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AlterField(
            model_name='order',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2015, 12, 4, 5, 12, 55, 74868, tzinfo=utc)),
            preserve_default=True,
        ),
    ]
