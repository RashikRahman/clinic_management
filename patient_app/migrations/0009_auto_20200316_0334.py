# Generated by Django 3.0.2 on 2020-03-15 21:34

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('patient_app', '0008_auto_20200208_1401'),
    ]

    operations = [
        migrations.AlterField(
            model_name='patient',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2020, 3, 16, 3, 34, 18, 980073)),
        ),
    ]
