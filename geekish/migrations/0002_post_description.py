# Generated by Django 3.0 on 2022-07-12 10:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('geekish', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='description',
            field=models.CharField(blank=True, max_length=60, null=True),
        ),
    ]