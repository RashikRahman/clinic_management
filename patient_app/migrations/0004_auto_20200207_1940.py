# Generated by Django 3.0.2 on 2020-02-07 13:40

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('patient_app', '0003_auto_20200207_1939'),
    ]

    operations = [
        migrations.AlterField(
            model_name='patient',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2020, 2, 7, 19, 40, 29, 375016)),
        ),
    ]
