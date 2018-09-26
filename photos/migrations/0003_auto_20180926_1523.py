# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-09-26 12:23
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('photos', '0002_auto_20180925_1946'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='image',
            options={'ordering': ['name']},
        ),
        migrations.AddField(
            model_name='image',
            name='posted_date',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]