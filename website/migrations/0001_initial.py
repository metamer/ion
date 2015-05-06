# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Page',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('page_text', models.TextField()),
                ('update_date', models.DateTimeField(verbose_name='date updated')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='PageCategory',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('category_name', models.CharField(max_length=200)),
                ('parent_category', models.ForeignKey(blank=True, to='website.PageCategory', null=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='page',
            name='page_category',
            field=models.ForeignKey(to='website.PageCategory'),
            preserve_default=True,
        ),
    ]
