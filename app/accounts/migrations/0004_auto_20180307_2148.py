# Generated by Django 2.0.2 on 2018-03-07 12:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_user_qiita_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='qiita_id',
            field=models.CharField(max_length=128, null=True, unique=True),
        ),
    ]
