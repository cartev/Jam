# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-09-29 01:39
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('jam', '0011_auto_20160928_2327'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='review',
            name='ArtistID',
        ),
        migrations.RemoveField(
            model_name='review',
            name='ReviewerProfile',
        ),
    ]
