# Generated by Django 3.0 on 2022-08-01 14:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('geekish', '0039_auto_20220801_1425'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='p_topic_1',
            field=models.CharField(blank=True, max_length=200),
        ),
        migrations.AlterField(
            model_name='post',
            name='p_topic_2',
            field=models.CharField(blank=True, max_length=200),
        ),
        migrations.AlterField(
            model_name='post',
            name='p_topic_3',
            field=models.CharField(blank=True, max_length=200),
        ),
        migrations.AlterField(
            model_name='post',
            name='p_topic_4',
            field=models.CharField(blank=True, max_length=200),
        ),
    ]