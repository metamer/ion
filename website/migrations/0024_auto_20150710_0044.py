# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0023_auto_20150710_0027'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='licenseitemlink',
            name='genericlink_ptr',
        ),
        migrations.RemoveField(
            model_name='licenseitemlink',
            name='license_usage',
        ),
        migrations.DeleteModel(
            name='LicenseItemLink',
        ),
    ]
