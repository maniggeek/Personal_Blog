# Generated by Django 3.0 on 2022-07-19 10:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('geekish', '0019_comment'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Comment',
        ),
    ]