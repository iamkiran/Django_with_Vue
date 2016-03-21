# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-03-20 10:07
from __future__ import unicode_literals

import articles.models
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=256, verbose_name=b'Title')),
                ('author_Detail', models.CharField(max_length=128, verbose_name=b'Author')),
                ('date', models.DateTimeField(verbose_name=b'Published Date')),
                ('m_image', models.ImageField(upload_to=articles.models.autogenerated_Main_Image_Name, verbose_name=b'Main Image ')),
                ('s_Image', models.ImageField(upload_to=articles.models.autogenerated_Sub_Image_Name, verbose_name=b'Sub Image')),
                ('body', models.TextField(verbose_name=b'Main Article')),
                ('likecount', models.TextField(blank=True, editable=False, max_length=1000, verbose_name=b'LikeCount')),
            ],
            options={
                'ordering': ['-date'],
                'verbose_name_plural': 'News',
            },
        ),
    ]