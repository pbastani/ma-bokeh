# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Curve',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, serialize=False, primary_key=True)),
                ('asOf', models.DateTimeField(verbose_name='Observation Date')),
                ('market_data_path', models.CharField(max_length=200)),
                ('processors_path', models.CharField(max_length=200)),
                ('constructors_path', models.CharField(max_length=200)),
            ],
        ),
    ]
