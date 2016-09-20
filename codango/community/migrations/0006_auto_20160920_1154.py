# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import multiselectfield.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ('community', '0005_auto_20160830_1052'),
    ]

    operations = [
        migrations.AlterField(
            model_name='community',
            name='default_group_permissions',
            field=multiselectfield.db.fields.MultiSelectField(default=[b'BLOCK_MEMBER'], max_length=55, verbose_name=b'Default Members Permissions', choices=[(b'INVITE_MEMBER', b'Send invites'), (b'DELETE_MEMBER', b'Remove members'), (b'BLOCK_MEMBER', b'Block members'), (b'SUSPEND_MEMBER', b'Suspend members')]),
        ),
        migrations.AlterField(
            model_name='community',
            name='description',
            field=models.TextField(max_length=1000),
        ),
        migrations.AlterField(
            model_name='community',
            name='name',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='community',
            name='private',
            field=models.BooleanField(default=False, verbose_name=b'Private (Default is Public)'),
        ),
        migrations.AlterField(
            model_name='community',
            name='visibility',
            field=models.CharField(default=b'full', max_length=30, choices=[(b'none', b'None'), (b'partial', b'Partial'), (b'full', b'Full')]),
        ),
        migrations.AlterField(
            model_name='communityblacklist',
            name='blacklist_type',
            field=models.CharField(default=b'Block', max_length=20, choices=[(b'block', b'Block'), (b'suspend', b'Suspend')]),
        ),
        migrations.AlterField(
            model_name='communitymember',
            name='permission',
            field=multiselectfield.db.fields.MultiSelectField(default=[b'BLOCK_MEMBER'], max_length=55, choices=[(b'INVITE_MEMBER', b'Send invites'), (b'DELETE_MEMBER', b'Remove members'), (b'BLOCK_MEMBER', b'Block members'), (b'SUSPEND_MEMBER', b'Suspend members')]),
        ),
        migrations.AlterUniqueTogether(
            name='community',
            unique_together=set([('name', 'creator')]),
        ),
        migrations.AlterUniqueTogether(
            name='communitymember',
            unique_together=set([('community', 'user')]),
        ),
    ]
