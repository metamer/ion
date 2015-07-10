# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0024_auto_20150710_0044'),
    ]

    operations = [
        migrations.AlterField(
            model_name='licenseusage',
            name='notes',
            field=models.TextField(blank=True, help_text='HTML for notes'),
        ),
    ]
