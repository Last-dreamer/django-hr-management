# Generated by Django 3.2.4 on 2021-06-03 05:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employee', '0008_alter_employees_dept'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employees',
            name='cnic',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
