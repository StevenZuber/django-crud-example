# Generated by Django 2.1.7 on 2019-03-13 17:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('demoAPI', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='avenger',
            name='avenger_name',
            field=models.CharField(default='', max_length=50),
        ),
    ]