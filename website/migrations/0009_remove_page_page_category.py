# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0008_page_page_category'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='page',
            name='page_category',
        ),
    ]
