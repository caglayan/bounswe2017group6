# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-11-14 20:21
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('components', '0008_auto_20171029_0057'),
    ]

    operations = [
        migrations.CreateModel(
            name='DateTimeComponent',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='LongTextComponent',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='NumberComponent',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data', models.DecimalField(decimal_places=5, max_digits=15)),
            ],
        ),
        migrations.CreateModel(
            name='TextComponent',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='VideoComponent',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data', models.URLField()),
            ],
        ),
        migrations.DeleteModel(
            name='Image',
        ),
        migrations.DeleteModel(
            name='Subtitle',
        ),
        migrations.DeleteModel(
            name='TextArea',
        ),
        migrations.DeleteModel(
            name='Title',
        ),
        migrations.DeleteModel(
            name='Video',
        ),
        migrations.RemoveField(
            model_name='component',
            name='content',
        ),
        migrations.RemoveField(
            model_name='component',
            name='long_text',
        ),
        migrations.RemoveField(
            model_name='component',
            name='small_text',
        ),
        migrations.RemoveField(
            model_name='component',
            name='url',
        ),
        migrations.AddField(
            model_name='component',
            name='name',
            field=models.CharField(default='', max_length=20),
        ),
        migrations.AlterField(
            model_name='component',
            name='component_type',
            field=models.CharField(choices=[('text', 'Text'), ('longtext', 'Long Text'), ('number', 'Number'), ('datetime', 'Date/Time'), ('image', 'Image'), ('video', 'Video'), ('dropdown', 'Dropdown'), ('checkbox', 'Checkbox')], default='text', max_length=10),
        ),
        migrations.AddField(
            model_name='component',
            name='datetime',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='components.DateTimeComponent'),
        ),
        migrations.AddField(
            model_name='component',
            name='longtext',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='components.LongTextComponent'),
        ),
        migrations.AddField(
            model_name='component',
            name='number',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='components.NumberComponent'),
        ),
        migrations.AddField(
            model_name='component',
            name='text',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='components.TextComponent'),
        ),
        migrations.AddField(
            model_name='component',
            name='video',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='components.VideoComponent'),
        ),
    ]