# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-09-30 01:04
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('day', '0018_auto_20160930_0952'),
    ]

    operations = [
        migrations.CreateModel(
            name='QuestionLevel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question_level_1', models.TextField(blank=True, verbose_name='レベル1')),
                ('question_level_2', models.TextField(blank=True, verbose_name='レベル2')),
                ('question_level_3', models.TextField(blank=True, verbose_name='レベル3')),
                ('question_level_4', models.TextField(blank=True, verbose_name='レベル4')),
                ('question_level_5', models.TextField(blank=True, verbose_name='レベル5')),
            ],
        ),
        migrations.AlterField(
            model_name='report',
            name='content_T',
            field=models.TextField(blank=True, verbose_name='次にすること(T)'),
        ),
        migrations.AlterField(
            model_name='report',
            name='content_W',
            field=models.TextField(blank=True, verbose_name='わかったこと(W)'),
        ),
        migrations.AlterField(
            model_name='report',
            name='content_Y',
            field=models.TextField(blank=True, verbose_name='やったこと(Y)'),
        ),
        migrations.AddField(
            model_name='questionlevel',
            name='report',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='levels', to='day.Report', verbose_name='日報'),
        ),
    ]