# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0003_page_page_shortname'),
    ]

    operations = [
        migrations.AddField(
            model_name='pagecategory',
            name='category_desc',
            field=models.CharField(default='Top level', max_length=200),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='pagecategory',
            name='category_name',
            field=models.CharField(max_length=20),
            preserve_default=True,
        ),
    ]
