# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-09-26 13:36
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('photos', '0003_auto_20180926_1523'),
    ]

    operations = [
        migrations.RenameField(
            model_name='image',
            old_name='categoies',
            new_name='categories',
        ),
    ]