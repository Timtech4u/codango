# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pairprogram', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='session',
            name='language',
            field=models.CharField(default=b'python', max_length=30),
        ),
        migrations.AddField(
            model_name='session',
            name='theme',
            field=models.CharField(default=b'cobalt', max_length=30),
        ),
    ]
