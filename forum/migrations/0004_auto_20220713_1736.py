# Generated by Django 3.2.13 on 2022-07-13 17:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('forum', '0003_auto_20220704_1232'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='post_image',
        ),
        migrations.AlterField(
            model_name='post',
            name='slug',
            field=models.CharField(max_length=100, unique=True),
        ),
    ]
