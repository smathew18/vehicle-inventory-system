# Generated by Django 2.2 on 2020-10-26 19:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vehiclemsapp', '0002_auto_20201026_2345'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vehicleavailability',
            name='vehicle_availabilityComments',
            field=models.CharField(default='', max_length=200),
        ),
    ]
