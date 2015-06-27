# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0018_auto_20150301_2343'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, primary_key=True, verbose_name='ID')),
                ('link', models.TextField(validators=[django.core.validators.URLValidator('Link must be a valid hyperlink')], help_text='Link to commented page')),
                ('link_title', models.CharField(help_text='Title of linked page ', max_length=200)),
                ('text', models.TextField(help_text='HTML comment')),
                ('pub_date', models.DateTimeField(help_text='Date comment was first published', verbose_name='date published')),
            ],
        ),
        migrations.AlterModelOptions(
            name='newsentry',
            options={'verbose_name_plural': 'News Entries'},
        ),
        migrations.AlterModelOptions(
            name='pagecategory',
            options={'verbose_name_plural': 'Page Categories'},
        ),
    ]
