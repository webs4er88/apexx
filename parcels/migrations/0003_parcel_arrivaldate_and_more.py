# Generated by Django 5.0.2 on 2024-03-05 17:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('parcels', '0002_alter_parcel_planned_delivery_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='parcel',
            name='Arrivaldate',
            field=models.CharField(default='March 2, 2024', max_length=200),
        ),
        migrations.AlterField(
            model_name='parcel',
            name='planned_delivery_date',
            field=models.CharField(default='March 12, 2024', max_length=200),
        ),
    ]
