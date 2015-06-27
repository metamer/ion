# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0020_auto_20150627_0019'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='link',
            field=models.URLField(validators=[django.core.validators.URLValidator('Link must be a valid hyperlink')], help_text='Link to commented page'),
        ),
    ]
