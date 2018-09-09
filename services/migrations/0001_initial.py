# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ServiceRequest',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('subject', models.CharField(max_length=50)),
                ('problem', models.CharField(max_length=255)),
                ('objective', models.CharField(max_length=255)),
                ('deadline', models.DateField(default='12/31/2018')),
                ('status', models.CharField(max_length=1, default='Open', choices=[(0, 'Open'), (1, 'Assigned'), (2, 'Completed'), (3, 'Terminated')])),
            ],
        ),
    ]
