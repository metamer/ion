# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pagecategory',
            name='parent_category',
        ),
        migrations.AddField(
            model_name='page',
            name='page_title',
            field=models.CharField(max_length=200, default='temp'),
            preserve_default=False,
        ),
    ]
