# Generated by Django 3.0.2 on 2020-01-18 17:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('department_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128)),
                ('cost', models.IntegerField(default=0)),
                ('duration', models.CharField(max_length=20)),
                ('department', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='services', to='department_app.Department')),
            ],
        ),
    ]
