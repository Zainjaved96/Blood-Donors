# Generated by Django 4.2.2 on 2023-09-09 06:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_alter_blooddonor_blood_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blooddonor',
            name='last_donation_date',
            field=models.DateField(blank=True, null=True),
        ),
    ]
