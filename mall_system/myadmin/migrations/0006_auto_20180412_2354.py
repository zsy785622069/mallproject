# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2018-04-12 15:54
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myadmin', '0005_users_delete_data'),
    ]

    operations = [
        migrations.AlterField(
            model_name='users',
            name='status',
            field=models.CharField(max_length=3),
        ),
    ]
