# Generated by Django 3.0.2 on 2020-03-15 21:42

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('invoice_app', '0005_auto_20200316_0341'),
    ]

    operations = [
        migrations.AlterField(
            model_name='invoice',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2020, 3, 16, 3, 42, 48, 845958)),
        ),
    ]
