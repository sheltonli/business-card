# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID', auto_created=True)),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(default=django.utils.timezone.now, verbose_name='last login')),
                ('email', models.CharField(max_length=254, unique=True)),
                ('full_name', models.CharField(max_length=100)),
                ('address', models.CharField(max_length=150)),
                ('address_2', models.CharField(max_length=150, blank=True)),
                ('city', models.CharField(max_length=100)),
                ('country', models.CharField(max_length=100)),
                ('province_state', models.CharField(max_length=100)),
                ('postal_code', models.CharField(max_length=20)),
                ('phone_number', models.CharField(max_length=20)),
                ('is_staff', models.BooleanField(default=False)),
                ('is_active', models.BooleanField(default=True)),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('updated_on', models.DateTimeField(auto_now=True)),
            ],
            options={
                'managed': True,
                'db_table': 'user',
            },
            bases=(models.Model,),
        ),
    ]
