# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-03-23 13:28
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('jam', '0004_album_spotifyalbumid'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='album',
            name='ArtsitName',
        ),
        migrations.DeleteModel(
            name='Album',
        ),
    ]
