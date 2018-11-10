# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import mptt.fields


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0005_genre'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='genre',
            name='parent',
        ),
        migrations.DeleteModel(
            name='Genre',
        ),
        migrations.AddField(
            model_name='pagecategory',
            name='level',
            field=models.PositiveIntegerField(editable=False, db_index=True, default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='pagecategory',
            name='lft',
            field=models.PositiveIntegerField(editable=False, db_index=True, default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='pagecategory',
            name='parent',
            field=mptt.fields.TreeForeignKey(on_delete=models.PROTECT, blank=True, to='website.PageCategory', related_name='children', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='pagecategory',
            name='rght',
            field=models.PositiveIntegerField(editable=False, db_index=True, default=2),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='pagecategory',
            name='tree_id',
            field=models.PositiveIntegerField(editable=False, db_index=True, default=0),
            preserve_default=False,
        ),
    ]
