# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0019_auto_20150627_0008'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='pub_date',
            field=models.DateTimeField(verbose_name='date published', auto_now=True, help_text='Date comment was first published'),
        ),
        migrations.AlterField(
            model_name='newsentry',
            name='pub_date',
            field=models.DateTimeField(verbose_name='date published', auto_now=True, help_text='Date page was first published'),
        ),
        migrations.AlterField(
            model_name='page',
            name='update_date',
            field=models.DateTimeField(verbose_name='date updated', auto_now=True, help_text='Date page was last updated'),
        ),
    ]
