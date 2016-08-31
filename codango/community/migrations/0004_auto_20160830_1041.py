# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('community', '0003_auto_20160824_1103'),
    ]

    operations = [
        migrations.RenameField(
            model_name='communitymember',
            old_name='user',
            new_name='creator',
        ),
        migrations.AlterField(
            model_name='community',
            name='visibility',
            field=models.CharField(default=b'Partial', max_length=30, choices=[(b'none', b'None'), (b'partial', b'Partial'), (b'full', b'Full')]),
        ),
        migrations.AlterField(
            model_name='communitymember',
            name='status',
            field=models.CharField(default=b'Pending', max_length=20, choices=[(b'pending', b'Pending'), (b'approved', b'Approved'), (b'declined', b'Declined')]),
        ),
    ]
