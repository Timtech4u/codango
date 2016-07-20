# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pairprogram', '0002_auto_20160720_1006'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='session',
            name='theme',
        ),
    ]
