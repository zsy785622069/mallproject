# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2018-04-11 06:21
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=64, unique=True)),
                ('password', models.CharField(max_length=128)),
                ('sex', models.CharField(max_length=3, null=True)),
                ('age', models.IntegerField(null=True)),
                ('address', models.CharField(max_length=128, null=True)),
                ('phone', models.CharField(max_length=11)),
                ('email', models.CharField(max_length=64)),
                ('status', models.IntegerField()),
                ('addtime', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
