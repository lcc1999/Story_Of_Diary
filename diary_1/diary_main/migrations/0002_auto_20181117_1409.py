# Generated by Django 2.1.1 on 2018-11-17 06:09

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('diary_main', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='diary',
            name='pub_date',
            field=models.DateTimeField(default=datetime.datetime(1970, 1, 1, 0, 0)),
        ),
    ]
