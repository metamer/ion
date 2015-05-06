# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0002_auto_20150212_0029'),
    ]

    operations = [
        migrations.AddField(
            model_name='page',
            name='page_shortname',
            field=models.CharField(max_length=20, default='top'),
            preserve_default=False,
        ),
    ]
