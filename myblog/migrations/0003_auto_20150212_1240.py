# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myblog', '0002_users'),
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('blog_id', models.AutoField(serialize=False, primary_key=True)),
                ('title', models.CharField(max_length=128, verbose_name=b'Titile')),
                ('content', models.TextField(verbose_name=b'Content')),
                ('pub_data', models.DateTimeField(auto_now_add=True)),
                ('edit_date', models.DateTimeField(auto_now=True)),
                ('user_id', models.ForeignKey(to='myblog.Users')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Cat_Blog_Map',
            fields=[
                ('map_id', models.AutoField(serialize=False, primary_key=True)),
                ('blog_id', models.ForeignKey(to='myblog.Blog')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('cat_id', models.AutoField(serialize=False, primary_key=True)),
                ('name', models.CharField(max_length=64, verbose_name=b'Category Name')),
                ('parent_id', models.ForeignKey(to='myblog.Category', blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('comment_id', models.AutoField(serialize=False, primary_key=True)),
                ('comment', models.TextField(verbose_name=b'Comment')),
                ('pub_date', models.DateTimeField(auto_now_add=True)),
                ('post_id', models.ForeignKey(to='myblog.Blog')),
                ('user_id', models.ForeignKey(to='myblog.Users')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Images',
            fields=[
                ('img_id', models.AutoField(serialize=False, primary_key=True)),
                ('img_name', models.CharField(max_length=64, verbose_name=b'Image Name')),
                ('img_url', models.CharField(max_length=256, verbose_name=b'Image URL')),
                ('blog_id', models.ForeignKey(to='myblog.Blog')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.RemoveField(
            model_name='post',
            name='author',
        ),
        migrations.DeleteModel(
            name='Post',
        ),
        migrations.AddField(
            model_name='cat_blog_map',
            name='cat_id',
            field=models.ForeignKey(to='myblog.Category'),
            preserve_default=True,
        ),
    ]
