# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0013_auto_20150301_1653'),
    ]

    operations = [
        migrations.AlterField(
            model_name='page',
            name='pub_date',
            field=models.DateTimeField(default=datetime.datetime(2015, 3, 2, 4, 5, 21, 506675, tzinfo=utc), help_text='Date page was first published', verbose_name='date published'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='page',
            name='update_date',
            field=models.DateTimeField(default=datetime.datetime(2015, 3, 2, 4, 5, 21, 506733, tzinfo=utc), help_text='Date page was last updated', verbose_name='date updated'),
            preserve_default=True,
        ),
    ]
