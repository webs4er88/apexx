# Generated by Django 5.0.2 on 2024-03-05 17:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('parcels', '0003_parcel_arrivaldate_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='parcel',
            name='statuscolor',
            field=models.CharField(default='green', max_length=200),
        ),
        migrations.AlterField(
            model_name='parcel',
            name='planned_delivery_date',
            field=models.CharField(default='leave void', max_length=200),
        ),
    ]
