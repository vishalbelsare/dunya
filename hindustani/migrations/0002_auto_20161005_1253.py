# -*- coding: utf-8 -*-
# Generated by Django 1.9.9 on 2016-10-05 10:53
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hindustani', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='artist',
            name='references',
        ),
        migrations.RemoveField(
            model_name='artist',
            name='source',
        ),
        migrations.RemoveField(
            model_name='composer',
            name='references',
        ),
        migrations.RemoveField(
            model_name='composer',
            name='source',
        ),
        migrations.RemoveField(
            model_name='form',
            name='references',
        ),
        migrations.RemoveField(
            model_name='form',
            name='source',
        ),
        migrations.RemoveField(
            model_name='instrument',
            name='references',
        ),
        migrations.RemoveField(
            model_name='instrument',
            name='source',
        ),
        migrations.RemoveField(
            model_name='laya',
            name='references',
        ),
        migrations.RemoveField(
            model_name='laya',
            name='source',
        ),
        migrations.RemoveField(
            model_name='raag',
            name='references',
        ),
        migrations.RemoveField(
            model_name='raag',
            name='source',
        ),
        migrations.RemoveField(
            model_name='recording',
            name='references',
        ),
        migrations.RemoveField(
            model_name='recording',
            name='source',
        ),
        migrations.RemoveField(
            model_name='release',
            name='references',
        ),
        migrations.RemoveField(
            model_name='release',
            name='source',
        ),
        migrations.RemoveField(
            model_name='taal',
            name='references',
        ),
        migrations.RemoveField(
            model_name='taal',
            name='source',
        ),
        migrations.RemoveField(
            model_name='work',
            name='references',
        ),
        migrations.RemoveField(
            model_name='work',
            name='source',
        ),
    ]
