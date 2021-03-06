# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-10-21 06:01
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('day', '0021_answerquestion'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment', models.TextField(blank=True, verbose_name='コメント')),
                ('comment_user', models.CharField(max_length=255, verbose_name='コメント投稿者')),
                ('comment_time', models.CharField(max_length=255, verbose_name='コメント時間')),
                ('report', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='day.Report', verbose_name='日報')),
            ],
        ),
        migrations.RemoveField(
            model_name='impression',
            name='report',
        ),
        migrations.AlterField(
            model_name='answerquestion',
            name='question',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='answers', to='day.Question', verbose_name='質問'),
        ),
        migrations.DeleteModel(
            name='Impression',
        ),
    ]
