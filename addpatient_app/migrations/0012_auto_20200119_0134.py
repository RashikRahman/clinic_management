# Generated by Django 3.0.2 on 2020-01-18 19:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('addpatient_app', '0011_auto_20200119_0119'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='addpatient',
            name='MedNAme',
        ),
        migrations.RemoveField(
            model_name='addpatient',
            name='PatientName',
        ),
        migrations.RemoveField(
            model_name='addpatient',
            name='advice',
        ),
        migrations.RemoveField(
            model_name='addpatient',
            name='blood_group',
        ),
        migrations.RemoveField(
            model_name='addpatient',
            name='complain',
        ),
        migrations.RemoveField(
            model_name='addpatient',
            name='date',
        ),
        migrations.RemoveField(
            model_name='addpatient',
            name='diabetes',
        ),
        migrations.RemoveField(
            model_name='addpatient',
            name='dose',
        ),
        migrations.RemoveField(
            model_name='addpatient',
            name='duration',
        ),
        migrations.RemoveField(
            model_name='addpatient',
            name='observation',
        ),
        migrations.RemoveField(
            model_name='medicine',
            name='name',
        ),
    ]
