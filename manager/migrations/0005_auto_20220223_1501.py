# Generated by Django 3.2.8 on 2022-02-23 21:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('manager', '0004_alter_project_client_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='client',
            name='client_id',
        ),
        migrations.RemoveField(
            model_name='employee',
            name='employee_ID',
        ),
        migrations.RemoveField(
            model_name='project',
            name='project_ID',
        ),
    ]
