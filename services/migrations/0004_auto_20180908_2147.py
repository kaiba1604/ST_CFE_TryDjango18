# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0003_auto_20180908_2116'),
    ]

    operations = [
        migrations.AlterField(
            model_name='servicerequest',
            name='status',
            field=models.CharField(max_length=1, blank=True, null=True, default='Open', choices=[(0, 'Open'), (1, 'Assigned'), (2, 'Completed'), (3, 'Terminated')]),
        ),
    ]
