# Generated by Django 2.0.2 on 2018-03-05 12:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('aggregator', '0002_auto_20180305_2026'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='qiitaentry',
            name='private',
        ),
    ]
