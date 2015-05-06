# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0006_auto_20150228_1603'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='page',
            name='page_category',
        ),
    ]
