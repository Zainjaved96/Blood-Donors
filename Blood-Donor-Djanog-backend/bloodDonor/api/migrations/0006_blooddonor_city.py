# Generated by Django 4.2.2 on 2023-09-10 09:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0005_alter_blooddonor_email_alter_blooddonor_phone_number'),
    ]

    operations = [
        migrations.AddField(
            model_name='blooddonor',
            name='city',
            field=models.CharField(default='Lahore', max_length=100),
        ),
    ]
