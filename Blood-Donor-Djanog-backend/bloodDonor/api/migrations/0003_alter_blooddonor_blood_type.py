# Generated by Django 4.2.2 on 2023-09-08 16:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_alter_blooddonor_phone_number'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blooddonor',
            name='blood_type',
            field=models.CharField(max_length=3),
        ),
    ]