# Generated by Django 3.2.3 on 2021-05-31 12:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employee_register', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Position',
            new_name='EmployeeSalary',
        ),
        migrations.RenameField(
            model_name='employee',
            old_name='position',
            new_name='salary',
        ),
        migrations.RenameField(
            model_name='employeesalary',
            old_name='title',
            new_name='salary',
        ),
        migrations.RemoveField(
            model_name='employee',
            name='mobile',
        ),
        migrations.AddField(
            model_name='employee',
            name='department',
            field=models.CharField(choices=[('J', 'Java'), ('P', 'Python'), ('L', 'Large')], default=1, max_length=1),
            preserve_default=False,
        ),
    ]
