# Generated by Django 3.2.3 on 2021-05-31 11:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Employee', '0013_remove_employee_emp_code'),
    ]

    operations = [
        migrations.AddField(
            model_name='employee',
            name='emp_code',
            field=models.CharField(default=1, max_length=3),
            preserve_default=False,
        ),
    ]
