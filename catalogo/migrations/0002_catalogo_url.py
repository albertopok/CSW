# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalogo', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='catalogo',
            name='url',
            field=models.TextField(default='no definido', max_length=500),
            preserve_default=False,
        ),
    ]
