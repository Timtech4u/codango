# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('community', '0004_auto_20160830_1041'),
    ]

    operations = [
        migrations.RenameField(
            model_name='community',
            old_name='user',
            new_name='creator',
        ),
        migrations.RenameField(
            model_name='communitymember',
            old_name='creator',
            new_name='user',
        ),
    ]
