# Generated by Django 3.0 on 2019-12-13 04:09

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('flowcharts', '0002_flowchart_last_updated'),
    ]

    operations = [
        migrations.AlterField(
            model_name='flowchart',
            name='last_updated',
            field=models.DateTimeField(default=datetime.datetime(2019, 12, 13, 4, 9, 36, 229614)),
        ),
    ]
