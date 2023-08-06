# Generated by Django 4.2 on 2023-08-06 15:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0007_department'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='department',
            name='departmentname',
        ),
        migrations.AddField(
            model_name='department',
            name='department',
            field=models.CharField(default='Cardiologist', max_length=250),
        ),
        migrations.DeleteModel(
            name='Patient',
        ),
    ]
