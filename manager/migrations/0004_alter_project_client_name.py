# Generated by Django 3.2.8 on 2022-02-23 20:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('manager', '0003_auto_20220223_1445'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='client_name',
            field=models.ForeignKey(default=' ', max_length=50, on_delete=django.db.models.deletion.DO_NOTHING, related_name='client', to='manager.client'),
        ),
    ]
