# Generated by Django 2.1.2 on 2018-11-10 18:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0001_squashed_0027_auto_20181110_1235'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pagecategory',
            name='category_desc',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='pagecategory',
            name='level',
            field=models.PositiveIntegerField(db_index=True, editable=False),
        ),
        migrations.AlterField(
            model_name='pagecategory',
            name='lft',
            field=models.PositiveIntegerField(db_index=True, editable=False),
        ),
        migrations.AlterField(
            model_name='pagecategory',
            name='rght',
            field=models.PositiveIntegerField(db_index=True, editable=False),
        ),
        migrations.AlterField(
            model_name='pagecategory',
            name='tree_id',
            field=models.PositiveIntegerField(db_index=True, editable=False),
        ),
    ]
