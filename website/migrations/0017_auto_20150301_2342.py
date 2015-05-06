# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0016_auto_20150301_2341'),
    ]

    operations = [
        migrations.AlterField(
            model_name='newsentry',
            name='pub_date',
            field=models.DateTimeField(verbose_name='date published', help_text='Date page was first published'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='page',
            name='pub_date',
            field=models.DateTimeField(verbose_name='date published', help_text='Date page was first published'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='page',
            name='update_date',
            field=models.DateTimeField(verbose_name='date updated', help_text='Date page was last updated'),
            preserve_default=True,
        ),
    ]
