# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import cloudinary.models
import multiselectfield.db.fields
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Community',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('date_modified', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=100)),
                ('logo', cloudinary.models.CloudinaryField(max_length=255, null=True, verbose_name=b'logo', blank=True)),
                ('description', models.TextField()),
                ('private', models.BooleanField(default=False)),
                ('visibility', models.CharField(default=b'Partial', max_length=30, choices=[(b'None', b'None'), (b'Partial', b'Partial'), (b'Full', b'Full')])),
                ('default_group_permissions', multiselectfield.db.fields.MultiSelectField(max_length=55, choices=[(b'INVITE_MEMBER', b'Send invites'), (b'DELETE_MEMBER', b'Remove members'), (b'BLOCK_MEMBER', b'Block members'), (b'SUSPEND_MEMBER', b'Suspend members')])),
            ],
            options={
                'ordering': ['-date_modified'],
            },
        ),
        migrations.CreateModel(
            name='CommunityBlacklist',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('date_modified', models.DateTimeField(auto_now=True)),
                ('blacklist_type', models.CharField(default=b'Block', max_length=20, choices=[(b'Block', b'Block'), (b'Suspend', b'Suspend')])),
                ('blacklister', models.ForeignKey(related_name='community_blacklister', to=settings.AUTH_USER_MODEL)),
                ('community', models.ForeignKey(to='community.Community')),
                ('user', models.ForeignKey(related_name='community_blacklist', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-date_modified'],
            },
        ),
        migrations.CreateModel(
            name='CommunityMember',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('date_modified', models.DateTimeField(auto_now=True)),
                ('status', models.CharField(default=b'Pending', max_length=20, choices=[(b'Pending', b'Pending'), (b'Approved', b'Approved'), (b'Declined', b'Declined')])),
                ('community', models.ForeignKey(related_name='members', to='community.Community')),
                ('invitor', models.ForeignKey(related_name='invited_by', to=settings.AUTH_USER_MODEL)),
                ('user', models.ForeignKey(related_name='member', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-date_modified'],
            },
        ),
        migrations.CreateModel(
            name='Permission',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('date_modified', models.DateTimeField(auto_now=True)),
                ('label', models.CharField(max_length=50)),
                ('description', models.TextField()),
            ],
            options={
                'ordering': ['-date_modified'],
            },
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('date_modified', models.DateTimeField(auto_now=True)),
                ('title', models.CharField(max_length=50)),
            ],
            options={
                'ordering': ['-date_modified'],
            },
        ),
        migrations.AddField(
            model_name='community',
            name='tags',
            field=models.ManyToManyField(to='community.Tag'),
        ),
        migrations.AddField(
            model_name='community',
            name='user',
            field=models.ForeignKey(related_name='communities', to=settings.AUTH_USER_MODEL),
        ),
    ]
