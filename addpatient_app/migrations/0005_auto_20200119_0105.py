# Generated by Django 3.0.2 on 2020-01-18 19:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('patient_app', '0001_initial'),
        ('addpatient_app', '0004_auto_20200119_0103'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='addpatient',
            name='PatientName',
        ),
        migrations.AddField(
            model_name='addpatient',
            name='Name',
            field=models.OneToOneField(default='', on_delete=django.db.models.deletion.CASCADE, related_name='addpatient', to='patient_app.Patient'),
        ),
    ]
