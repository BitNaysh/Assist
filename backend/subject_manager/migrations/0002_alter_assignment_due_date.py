# Generated by Django 4.2 on 2023-04-21 01:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('subject_manager', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='assignment',
            name='due_date',
            field=models.DateTimeField(),
        ),
    ]
