# Generated by Django 3.0.2 on 2020-03-19 14:25

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('patient_app', '0014_auto_20200318_2342'),
    ]

    operations = [
        migrations.AlterField(
            model_name='patient',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2020, 3, 19, 20, 25, 6, 247956)),
        ),
    ]
