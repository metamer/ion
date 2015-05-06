# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0017_auto_20150301_2342'),
    ]

    operations = [
        migrations.AlterField(
            model_name='page',
            name='page_text',
            field=models.TextField(help_text='HTML content of page', blank=True),
            preserve_default=True,
        ),
    ]
