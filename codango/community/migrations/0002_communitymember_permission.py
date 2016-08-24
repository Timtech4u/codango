# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import multiselectfield.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ('community', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='communitymember',
            name='permission',
            field=multiselectfield.db.fields.MultiSelectField(max_length=55, null=True, choices=[(b'INVITE_MEMBER', b'Send invites'), (b'DELETE_MEMBER', b'Remove members'), (b'BLOCK_MEMBER', b'Block members'), (b'SUSPEND_MEMBER', b'Suspend members')]),
        ),
    ]
