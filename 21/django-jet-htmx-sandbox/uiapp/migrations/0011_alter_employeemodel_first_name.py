# Generated by Django 4.1 on 2022-08-13 18:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('uiapp', '0010_employeemodel_department_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employeemodel',
            name='first_name',
            field=models.CharField(max_length=20),
        ),
    ]