# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import cloudinary.models


class Migration(migrations.Migration):

    dependencies = [
        ('community', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='community',
            name='logo',
            field=cloudinary.models.CloudinaryField(max_length=255, null=True, verbose_name=b'logo'),
        ),
    ]
