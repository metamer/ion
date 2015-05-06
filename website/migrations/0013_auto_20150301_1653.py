# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0012_auto_20150301_1649'),
    ]

    operations = [
        migrations.AlterField(
            model_name='page',
            name='page_shortname',
            field=models.CharField(help_text='Short name of page (no special chars or spaces). This will be used for the url location of the page. Use _ to separate words.', max_length=20, validators=[django.core.validators.RegexValidator('^[\\w]+$', message='shortname must be alphanumeric')]),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='page',
            name='pub_date',
            field=models.DateTimeField(help_text='Date page was first published', editable=False, verbose_name='date published', default=datetime.datetime(2015, 3, 1, 21, 53, 17, 109507, tzinfo=utc)),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='page',
            name='update_date',
            field=models.DateTimeField(help_text='Date page was last updated', verbose_name='date updated', default=datetime.datetime(2015, 3, 1, 21, 53, 17, 109721, tzinfo=utc)),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='pagecategory',
            name='category_name',
            field=models.CharField(max_length=20, validators=[django.core.validators.RegexValidator('^[\\w]+$', message='category name must be alphanumeric')], unique=True),
            preserve_default=True,
        ),
    ]
