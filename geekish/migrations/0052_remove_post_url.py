# Generated by Django 3.0 on 2022-08-26 08:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('geekish', '0051_auto_20220826_0800'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='url',
        ),
    ]
