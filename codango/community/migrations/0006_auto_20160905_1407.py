# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('community', '0005_auto_20160830_1052'),
    ]

    operations = [
        migrations.AlterField(
            model_name='communityblacklist',
            name='blacklist_type',
            field=models.CharField(default=b'Block', max_length=20, choices=[(b'block', b'Block'), (b'suspend', b'Suspend')]),
        ),
    ]
