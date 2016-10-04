# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('community', '0008_merge'),
    ]

    operations = [
        migrations.AddField(
            model_name='addon',
            name='description',
            field=models.TextField(default=b'Basic addon description', max_length=1000),
        ),
    ]
