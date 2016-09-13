# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-09-13 22:40
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('bookmarks', '0005_sharedbookmark'),
    ]

    operations = [
        migrations.CreateModel(
            name='Friendship',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('from_friend', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='friend_set', to=settings.AUTH_USER_MODEL)),
                ('to_friend', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='to_friend_set', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
