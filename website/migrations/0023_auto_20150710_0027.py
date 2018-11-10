# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0022_auto_20150627_0032'),
    ]

    operations = [
        migrations.CreateModel(
            name='GenericLink',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
                ('name', models.CharField(help_text='Name', max_length=200)),
                ('link', models.URLField(help_text='Link')),
            ],
        ),
        migrations.CreateModel(
            name='LicenseUsage',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
                ('item', models.CharField(help_text='Name of item', max_length=200)),
                ('source_name', models.CharField(help_text='Name of source', max_length=200)),
                ('source_link', models.URLField(help_text='Link to commented page')),
                ('attribution', models.TextField(help_text='HTML for attribution')),
                ('usage', models.TextField(help_text='HTML for usage')),
                ('notes', models.TextField(help_text='HTML for notes')),
            ],
        ),
        migrations.CreateModel(
            name='License',
            fields=[
                ('genericlink_ptr',
                    models.OneToOneField(on_delete=models.PROTECT, serialize=False, to='website.GenericLink', primary_key=True, auto_created=True, parent_link=True)),
            ],
            bases=('website.genericlink',),
        ),
        migrations.CreateModel(
            name='LicenseItemLink',
            fields=[
                ('genericlink_ptr',
                    models.OneToOneField(on_delete=models.PROTECT, serialize=False, to='website.GenericLink', primary_key=True, auto_created=True, parent_link=True)),
            ],
            bases=('website.genericlink',),
        ),
        migrations.AddField(
            model_name='licenseusage',
            name='license',
            field=models.ForeignKey(on_delete=models.PROTECT, to='website.License'),
        ),
        migrations.AddField(
            model_name='licenseitemlink',
            name='license_usage',
            field=models.ForeignKey(on_delete=models.PROTECT, to='website.LicenseUsage'),
        ),
    ]
