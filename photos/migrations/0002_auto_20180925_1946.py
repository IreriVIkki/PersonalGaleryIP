# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-09-25 16:46
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('photos', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Category',
            new_name='categories',
        ),
        migrations.RemoveField(
            model_name='image',
            name='category',
        ),
        migrations.AddField(
            model_name='image',
            name='categoies',
            field=models.ManyToManyField(to='photos.categories'),
        ),
    ]