# Generated by Django 3.0.2 on 2020-03-16 14:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('appointment_app', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='appointment',
            old_name='no',
            new_name='phone',
        ),
    ]
