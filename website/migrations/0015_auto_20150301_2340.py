# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.utils.timezone import utc
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0014_auto_20150301_2305'),
    ]

    operations = [
        migrations.CreateModel(
            name='NewsEntry',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, verbose_name='ID', primary_key=True)),
                ('title', models.CharField(help_text='Title of the news entry', max_length=200)),
                ('text', models.TextField(help_text='HTML content of page')),
                ('pub_date', models.DateTimeField(verbose_name='date published', help_text='Date page was first published', default=datetime.datetime(2015, 3, 2, 4, 40, 39, 474373, tzinfo=utc))),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AlterField(
            model_name='page',
            name='pub_date',
            field=models.DateTimeField(verbose_name='date published', help_text='Date page was first published', default=datetime.datetime(2015, 3, 2, 4, 40, 39, 473317, tzinfo=utc)),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='page',
            name='update_date',
            field=models.DateTimeField(verbose_name='date updated', help_text='Date page was last updated', default=datetime.datetime(2015, 3, 2, 4, 40, 39, 473373, tzinfo=utc)),
            preserve_default=True,
        ),
    ]
