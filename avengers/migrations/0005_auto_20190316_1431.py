# Generated by Django 2.1.7 on 2019-03-16 20:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('avengers', '0004_auto_20190316_1358'),
    ]

    operations = [
        migrations.AlterField(
            model_name='avenger',
            name='slug',
            field=models.SlugField(blank=True),
        ),
    ]
