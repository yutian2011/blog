# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myblog', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Users',
            fields=[
                ('user_id', models.AutoField(serialize=False, primary_key=True)),
                ('user_name', models.CharField(max_length=32, verbose_name=b'User Name')),
                ('passwd', models.CharField(max_length=64, verbose_name=b'User Passwd')),
                ('email', models.EmailField(max_length=75)),
                ('register_date', models.DateTimeField(auto_now_add=True)),
                ('last_login_date', models.DateTimeField(auto_now=True)),
                ('last_ip', models.CharField(max_length=32, verbose_name=b'User login ip address')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
