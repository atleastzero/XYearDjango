# Generated by Django 3.0 on 2019-12-13 05:09

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('flowcharts', '0004_auto_20191213_0409'),
    ]

    operations = [
        migrations.AddField(
            model_name='flowchart',
            name='creates',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='flowchart',
            name='last_updated',
            field=models.DateTimeField(auto_now=True),
        ),
    ]