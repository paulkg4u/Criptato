# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='GroupAdminInfo',
            fields=[
                ('entry_id', models.AutoField(serialize=False, primary_key=True)),
                ('group_admin', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='GroupInfo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('group_name', models.CharField(max_length=100)),
                ('group_desc', models.TextField(default=b'')),
                ('public_key', models.CharField(max_length=50)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='TableData',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('table_name', models.CharField(max_length=100)),
                ('table_desc', models.TextField(default=b'')),
                ('table_data', models.TextField(default=b'')),
                ('table_owner', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='groupadmininfo',
            name='group_name',
            field=models.ForeignKey(to='ssapp.GroupInfo'),
            preserve_default=True,
        ),
    ]
