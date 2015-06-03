# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('ssapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='GroupData',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('group_name', models.CharField(max_length=100)),
                ('group_desc', models.TextField(default=b'')),
                ('group_members', models.ManyToManyField(to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='TableOwnerInfo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('group_name', models.ForeignKey(to='ssapp.GroupData')),
                ('table_name', models.ForeignKey(to='ssapp.TableData')),
                ('table_owner', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AlterField(
            model_name='groupadmininfo',
            name='group_name',
            field=models.ForeignKey(to='ssapp.GroupData'),
            preserve_default=True,
        ),
        migrations.DeleteModel(
            name='GroupInfo',
        ),
    ]
