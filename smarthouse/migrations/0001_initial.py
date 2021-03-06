# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-07-14 12:13
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Arduino',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('crypto_key', models.CharField(max_length=40)),
                ('conn_type', models.CharField(choices=[('bl', 'BLUETOOTH'), ('wf', 'WIFI'), ('rd', 'RADIO_433')], default='wf', max_length=2)),
                ('ip', models.GenericIPAddressField()),
                ('port', models.IntegerField()),
                ('name_bluetooth', models.CharField(max_length=20)),
                ('channel', models.IntegerField()),
            ],
        ),
    ]
