# Generated by Django 4.0.2 on 2022-02-21 03:40

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('project_name', models.CharField(default=' ', max_length=50)),
                ('project_ID', models.CharField(default=' ', max_length=50)),
                ('project_description', models.CharField(default=' ', max_length=50)),
                ('start_date', models.DateField(blank=True, null=True)),
                ('end_date', models.DateField(blank=True, null=True)),
                ('client_name', models.CharField(default=' ', max_length=50)),
                ('client_id', models.CharField(default=' ', max_length=50)),
                ('SOW_no', models.CharField(default=' ', max_length=50)),
                ('total_headcount', models.IntegerField(default=' ', max_length=20)),
                ('manager', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('employee_name', models.CharField(default=' ', max_length=50)),
                ('employee_ID', models.CharField(default=' ', max_length=50)),
                ('first_name', models.CharField(default=' ', max_length=50)),
                ('last_name', models.CharField(default=' ', max_length=50)),
                ('Email', models.EmailField(default=' ', max_length=100)),
                ('DOJ', models.DateField(blank=True, null=True)),
                ('Location', models.CharField(default=' ', max_length=50)),
                ('Designation', models.CharField(default=' ', max_length=50)),
                ('Assigned_project', models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='project', to='manager.project')),
                ('Project_manager', models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='manager', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
