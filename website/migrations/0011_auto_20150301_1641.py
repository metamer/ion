# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.utils.timezone import utc
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0010_page_page_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='page',
            name='page_description',
            field=models.CharField(blank=True, help_text='Description of page', max_length=500),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='page',
            name='pub_date',
            field=models.DateTimeField(default=datetime.datetime(2015, 3, 1, 21, 41, 9, 948611, tzinfo=utc), verbose_name='date published', help_text='Date page was first published'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='page',
            name='update_comment',
            field=models.CharField(blank=True, help_text='Changes made during last update', max_length=500),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='page',
            name='page_shortname',
            field=models.CharField(help_text='Short name of page (no special chars or spaces). This will be used for the url location of the page. Use _ to separate words.', max_length=20),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='page',
            name='page_text',
            field=models.TextField(help_text='HTML content of page'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='page',
            name='page_title',
            field=models.CharField(help_text='Title of the page', max_length=200),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='page',
            name='update_date',
            field=models.DateTimeField(default=datetime.datetime(2015, 3, 1, 21, 41, 9, 948664, tzinfo=utc), verbose_name='date updated', help_text='Date page was last updated'),
            preserve_default=True,
        ),
    ]
