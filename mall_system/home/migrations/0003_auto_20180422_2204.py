# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2018-04-22 14:04
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_auto_20180422_2108'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='usersaddress',
            name='usersid',
        ),
        migrations.RemoveField(
            model_name='order',
            name='addressid',
        ),
        migrations.AddField(
            model_name='order',
            name='addcode',
            field=models.IntegerField(default='123456'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='order',
            name='addname',
            field=models.CharField(default='123', max_length=32),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='order',
            name='addphone',
            field=models.CharField(default='123', max_length=11),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='order',
            name='address',
            field=models.CharField(default='123', max_length=128),
            preserve_default=False,
        ),
        migrations.DeleteModel(
            name='UsersAddress',
        ),
    ]
