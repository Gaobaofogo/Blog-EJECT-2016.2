# -*- coding: utf-8 -*-
# Generated by Django 1.10a1 on 2016-06-17 14:25
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_auto_20160617_1054'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='catagoria',
            new_name='categoria',
        ),
    ]
