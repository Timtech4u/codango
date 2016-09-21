# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('community', '0006_auto_20160921_1342'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='AddOnModel',
            new_name='AddOn',
        ),
    ]
