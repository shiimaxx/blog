# Generated by Django 2.0.2 on 2018-03-05 11:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('aggregator', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='qiitaentry',
            name='body',
        ),
        migrations.RemoveField(
            model_name='qiitaentry',
            name='comments_count',
        ),
        migrations.RemoveField(
            model_name='qiitaentry',
            name='like_count',
        ),
        migrations.RemoveField(
            model_name='qiitaentry',
            name='page_views_count',
        ),
        migrations.RemoveField(
            model_name='qiitaentry',
            name='reactions_count',
        ),
        migrations.RemoveField(
            model_name='qiitaentry',
            name='rendered_body',
        ),
        migrations.RemoveField(
            model_name='qiitaentry',
            name='updated_at',
        ),
    ]