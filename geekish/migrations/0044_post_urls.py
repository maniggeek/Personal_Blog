# Generated by Django 3.0 on 2022-08-18 13:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('geekish', '0043_remove_post_url'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='urls',
            field=models.URLField(default='', verbose_name=[]),
            preserve_default=False,
        ),
    ]