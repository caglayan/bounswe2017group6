# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-28 20:51
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('content', '0006_auto_20171028_2351'),
        ('group', '0002_remove_interestgroup_content_types'),
    ]

    operations = [
        migrations.AddField(
            model_name='interestgroup',
            name='content_types',
            field=models.ManyToManyField(to='content.ContentType'),
        ),
    ]