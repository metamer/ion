# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0015_auto_20150301_2340'),
    ]

    operations = [
        migrations.AlterField(
            model_name='newsentry',
            name='pub_date',
            field=models.DateTimeField(verbose_name='date published', help_text='Date page was first published', default=datetime.datetime(2015, 3, 2, 4, 41, 44, 973556, tzinfo=utc)),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='page',
            name='pub_date',
            field=models.DateTimeField(verbose_name='date published', help_text='Date page was first published', default=datetime.datetime(2015, 3, 2, 4, 41, 44, 972473, tzinfo=utc)),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='page',
            name='update_date',
            field=models.DateTimeField(verbose_name='date updated', help_text='Date page was last updated', default=datetime.datetime(2015, 3, 2, 4, 41, 44, 972528, tzinfo=utc)),
            preserve_default=True,
        ),
    ]
