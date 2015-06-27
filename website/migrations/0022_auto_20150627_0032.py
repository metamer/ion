# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0021_auto_20150627_0026'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='link',
            field=models.URLField(help_text='Link to commented page'),
        ),
    ]
