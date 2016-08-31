# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import multiselectfield.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ('community', '0002_communitymember_permission'),
    ]

    operations = [
        migrations.AlterField(
            model_name='community',
            name='default_group_permissions',
            field=multiselectfield.db.fields.MultiSelectField(default=b'Block members', max_length=55, choices=[(b'INVITE_MEMBER', b'Send invites'), (b'DELETE_MEMBER', b'Remove members'), (b'BLOCK_MEMBER', b'Block members'), (b'SUSPEND_MEMBER', b'Suspend members')]),
        ),
        migrations.AlterField(
            model_name='communitymember',
            name='permission',
            field=multiselectfield.db.fields.MultiSelectField(default=b'Block members', max_length=55, choices=[(b'INVITE_MEMBER', b'Send invites'), (b'DELETE_MEMBER', b'Remove members'), (b'BLOCK_MEMBER', b'Block members'), (b'SUSPEND_MEMBER', b'Suspend members')]),
        ),
    ]
