# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('resources', '0003_resource_community'),
    ]

    operations = [
        migrations.AlterField(
            model_name='resource',
            name='community',
            field=models.ForeignKey(related_name='resources', blank=True, to='community.Community', null=True),
        ),
    ]
