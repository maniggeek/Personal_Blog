# Generated by Django 3.0 on 2022-08-01 13:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('geekish', '0037_remove_comment_parent'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='body',
            field=models.TextField(blank=True),
        ),
    ]
