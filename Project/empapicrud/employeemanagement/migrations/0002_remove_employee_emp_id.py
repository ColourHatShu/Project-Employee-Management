# Generated by Django 3.2.3 on 2021-05-30 06:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('employeemanagement', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='employee',
            name='emp_id',
        ),
    ]
