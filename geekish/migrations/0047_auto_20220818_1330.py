# Generated by Django 3.0 on 2022-08-18 13:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('geekish', '0046_auto_20220818_1319'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='url',
            new_name='slug',
        ),
    ]