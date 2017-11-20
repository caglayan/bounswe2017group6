# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-11-18 22:24
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('content', '0012_auto_20171118_2354'),
    ]

    operations = [
        migrations.AddField(
            model_name='updown',
            name='created_date',
            field=models.DateTimeField(auto_now_add=True, default='2010-10-10 19:00'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='updown',
            name='modified_date',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='comment',
            name='content',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='content.Content'),
        ),
    ]