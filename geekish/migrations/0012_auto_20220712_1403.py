# Generated by Django 3.0 on 2022-07-12 14:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('geekish', '0011_post_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='image',
            field=models.ImageField(blank=True, upload_to='media/images/%Y/%m/%d/'),
        ),
    ]
