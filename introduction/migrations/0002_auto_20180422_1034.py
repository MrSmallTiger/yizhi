# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2018-04-22 10:34
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('introduction', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Goods',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('new_goods_url', models.URLField(verbose_name='\u6700\u65b0\u6210\u679c')),
                ('recommend_url', models.URLField(verbose_name='\u7cbe\u54c1\u63a8\u8350')),
                ('hot_goods_url', models.URLField(verbose_name='\u6700\u71b1\u5546\u54c1')),
                ('add_time', models.DateField(default=datetime.datetime.now, verbose_name='\u6dfb\u52a0\u65f6\u95f4')),
            ],
            options={
                'verbose_name': '\u6d4f\u89c8\u5546\u54c1',
                'verbose_name_plural': '\u6d4f\u89c8\u5546\u54c1',
            },
        ),
        migrations.AlterModelOptions(
            name='aboutplat',
            options={'verbose_name': '\u5173\u4e8e\u5e73\u53f0', 'verbose_name_plural': '\u5173\u4e8e\u5e73\u53f0'},
        ),
        migrations.AlterModelOptions(
            name='banner',
            options={'verbose_name': '\u8f6e\u64ad\u56fe', 'verbose_name_plural': '\u8f6e\u64ad\u56fe'},
        ),
        migrations.AlterModelOptions(
            name='maintechnology',
            options={'verbose_name': '\u79d1\u6280\u4ecb\u7d39', 'verbose_name_plural': '\u79d1\u6280\u4ecb\u7d39'},
        ),
        migrations.AddField(
            model_name='maintechnology',
            name='add_time',
            field=models.DateField(default=datetime.datetime.now, verbose_name='\u6dfb\u52a0\u65f6\u95f4'),
        ),
        migrations.AddField(
            model_name='maintechnology',
            name='image',
            field=models.ImageField(default='', upload_to='technologyes/%y/%m', verbose_name='\u56fe\u7247'),
        ),
        migrations.AddField(
            model_name='maintechnology',
            name='technology',
            field=models.TextField(default='', verbose_name='\u79d1\u6280\u4ecb\u7d39'),
        ),
        migrations.AlterField(
            model_name='aboutplat',
            name='aboutplat',
            field=models.TextField(verbose_name='\u5173\u4e8e\u5e73\u53f0'),
        ),
        migrations.AlterField(
            model_name='aboutplat',
            name='add_time',
            field=models.DateField(default=datetime.datetime.now, verbose_name='\u6dfb\u52a0\u65f6\u95f4'),
        ),
        migrations.AlterField(
            model_name='aboutplat',
            name='image',
            field=models.ImageField(upload_to='plat/%y/%m', verbose_name='\u56fe\u7247'),
        ),
        migrations.AlterField(
            model_name='banner',
            name='add_time',
            field=models.DateField(default=datetime.datetime.now, verbose_name='\u6dfb\u52a0\u65f6\u95f4'),
        ),
        migrations.AlterField(
            model_name='banner',
            name='image',
            field=models.ImageField(upload_to='banner/%y/%m', verbose_name='\u8f6e\u64ad\u56fe'),
        ),
        migrations.AlterField(
            model_name='banner',
            name='index',
            field=models.IntegerField(default=100, verbose_name='\u987a\u5e8f'),
        ),
        migrations.AlterField(
            model_name='banner',
            name='title',
            field=models.CharField(max_length=100, verbose_name='\u6807\u9898'),
        ),
        migrations.AlterField(
            model_name='banner',
            name='url',
            field=models.URLField(verbose_name='\u8bbf\u95ee\u5730\u5740'),
        ),
    ]
