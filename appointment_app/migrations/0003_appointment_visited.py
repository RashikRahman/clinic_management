# Generated by Django 3.0.2 on 2020-03-16 18:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appointment_app', '0002_auto_20200316_2027'),
    ]

    operations = [
        migrations.AddField(
            model_name='appointment',
            name='visited',
            field=models.BooleanField(default=False),
        ),
    ]
