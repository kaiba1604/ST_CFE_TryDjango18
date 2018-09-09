# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('newsletter', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='signup',
            name='FirstName',
            field=models.CharField(verbose_name='First Name', max_length=50, default='First'),
        ),
        migrations.AlterField(
            model_name='signup',
            name='LastName',
            field=models.CharField(verbose_name='Last Name', max_length=50, default='Last'),
        ),
    ]
