# Generated by Django 3.0.2 on 2020-03-18 17:42

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('patient_app', '0013_auto_20200317_0038'),
    ]

    operations = [
        migrations.AlterField(
            model_name='patient',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2020, 3, 18, 23, 42, 53, 78800)),
        ),
    ]
