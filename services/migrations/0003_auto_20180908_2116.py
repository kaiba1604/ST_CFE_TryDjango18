# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('services', '0002_servicerequest_requested'),
    ]

    operations = [
        migrations.AddField(
            model_name='servicerequest',
            name='manager',
            field=models.ForeignKey(blank=True, null=True, related_name='manager', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='servicerequest',
            name='staff',
            field=models.ForeignKey(blank=True, null=True, related_name='staff', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='servicerequest',
            name='requested',
            field=models.ForeignKey(blank=True, null=True, related_name='requested', to=settings.AUTH_USER_MODEL),
        ),
    ]
