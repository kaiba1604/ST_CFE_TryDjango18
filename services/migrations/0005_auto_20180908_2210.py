# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.utils.timezone import utc
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0004_auto_20180908_2147'),
    ]

    operations = [
        migrations.AddField(
            model_name='servicerequest',
            name='created',
            field=models.DateTimeField(default=datetime.datetime(2018, 9, 9, 3, 9, 55, 848858, tzinfo=utc), auto_now_add=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='servicerequest',
            name='updated',
            field=models.DateTimeField(default=datetime.datetime(2018, 9, 9, 3, 10, 0, 216049, tzinfo=utc), auto_now=True),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='servicerequest',
            name='status',
            field=models.CharField(max_length=1, blank=True, null=True, default='Open', choices=[('0', 'Open'), ('1', 'Assigned'), ('2', 'Completed'), ('3', 'Terminated')]),
        ),
    ]
