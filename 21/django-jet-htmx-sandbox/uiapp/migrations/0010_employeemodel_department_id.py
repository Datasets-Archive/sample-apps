# Generated by Django 4.1 on 2022-08-04 19:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('uiapp', '0009_remove_employeemodel_department_id_departmentsmodel'),
    ]

    operations = [
        migrations.AddField(
            model_name='employeemodel',
            name='department_id',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='uiapp.departmentsmodel'),
        ),
    ]