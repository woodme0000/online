# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2017-06-27 23:20
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='openid',
            field=models.CharField(default=b'', max_length=100, verbose_name=b'\xe5\xbe\xae\xe4\xbf\xa1openid'),
        ),
    ]
