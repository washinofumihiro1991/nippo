# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-09-30 00:52
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('day', '0017_auto_20160914_1626'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='report',
            name='content',
        ),
        migrations.AddField(
            model_name='report',
            name='content_T',
            field=models.TextField(blank=True, verbose_name='次にすること'),
        ),
        migrations.AddField(
            model_name='report',
            name='content_W',
            field=models.TextField(blank=True, verbose_name='わかったこと'),
        ),
        migrations.AddField(
            model_name='report',
            name='content_Y',
            field=models.TextField(blank=True, verbose_name='やったこと'),
        ),
    ]
