# Generated by Django 4.0.2 on 2022-02-21 04:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('manager', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='employee',
            name='Assigned_project',
        ),
        migrations.AlterField(
            model_name='project',
            name='total_headcount',
            field=models.IntegerField(default=' '),
        ),
    ]