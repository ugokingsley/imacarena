# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-09-06 23:48
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookmarks', '0003_userprofile'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64, unique=True)),
                ('bookmarks', models.ManyToManyField(to='bookmarks.Bookmark')),
            ],
        ),
    ]