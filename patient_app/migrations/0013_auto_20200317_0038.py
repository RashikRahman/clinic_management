# Generated by Django 3.0.2 on 2020-03-16 18:38

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('patient_app', '0012_auto_20200316_2027'),
    ]

    operations = [
        migrations.AlterField(
            model_name='patient',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2020, 3, 17, 0, 38, 5, 965696)),
        ),
    ]
