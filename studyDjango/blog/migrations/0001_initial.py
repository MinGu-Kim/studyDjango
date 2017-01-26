# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('reg_date', models.DateTimeField(auto_created=True, auto_now=True)),
                ('title', models.CharField(max_length=256)),
                ('content', models.CharField(max_length=2048)),
            ],
        ),
    ]
