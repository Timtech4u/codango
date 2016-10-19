# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('community', '0001_initial'),
        ('resources', '0002_notificationqueue'),
    ]

    operations = [
        migrations.AddField(
            model_name='resource',
            name='community',
            field=models.ForeignKey(
                blank=True, to='community.Community', null=True),
        ),
    ]
