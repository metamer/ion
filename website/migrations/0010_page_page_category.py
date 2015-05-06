# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0009_remove_page_page_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='page',
            name='page_category',
            field=models.ForeignKey(default=17, to='website.PageCategory'),
            preserve_default=False,
        ),
    ]
