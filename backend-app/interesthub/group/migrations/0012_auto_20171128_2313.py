# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-11-28 20:13
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('group', '0011_auto_20171128_1509'),
    ]

    operations = [
        migrations.AlterField(
            model_name='interestgroup',
            name='cover_img',
            field=models.ImageField(blank=True, max_length=254, null=True, upload_to='group/'),
        ),
        migrations.AlterField(
            model_name='interestgroup',
            name='logo_img',
            field=models.ImageField(blank=True, max_length=254, null=True, upload_to='group/'),
        ),
    ]
