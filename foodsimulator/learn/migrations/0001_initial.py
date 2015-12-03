# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.conf import settings
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='order',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('date', models.DateTimeField(default=datetime.datetime(2015, 12, 3, 10, 46, 39, 174579, tzinfo=utc))),
                ('students_present', models.IntegerField(default=0)),
                ('students_total', models.IntegerField(default=0)),
                ('units_delievered', models.IntegerField(default=0)),
                ('units_left', models.IntegerField(default=0)),
                ('feedback', models.CharField(max_length=200)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='school',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('school_name', models.CharField(max_length=200)),
                ('school_strength', models.IntegerField()),
                ('school_deliveryBoy', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='order',
            name='school',
            field=models.ForeignKey(to='learn.school'),
            preserve_default=True,
        ),
    ]
