# Generated by Django 5.0.2 on 2024-03-05 16:48

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Parcel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tracking_number', models.CharField(default='Track', max_length=200, unique=True)),
                ('delivery_progress', models.CharField(default='25', max_length=200)),
                ('from_location', models.CharField(default='1745 Bassel Street Reserve, LA 70084', max_length=200)),
                ('to_location', models.CharField(default='4509 Beechwood Avenue Cedar Knolls, NJ 07927', max_length=200)),
                ('shipment_status', models.CharField(default='ON TRANSIT', max_length=200)),
                ('current_location', models.CharField(default='AIRPORT CALIFORNIA, BAYWATCH OTC 123', max_length=200)),
                ('agent_phone', models.CharField(default='+1 533 363 2735', max_length=200)),
                ('sender_name', models.CharField(default='NGUC CHIA', max_length=200)),
                ('sender_location', models.CharField(default='FRANKFURT, GERMANY', max_length=200)),
                ('service_type', models.CharField(default='AIR FREIGHT', max_length=200)),
                ('recipient_name', models.CharField(default='JAMES V HENSFORD', max_length=200)),
                ('recipient_number', models.CharField(default='+1 625 737 328', max_length=200)),
                ('recipient_location', models.CharField(default='1745 Bassel Street Reserve, LA 70084', max_length=200)),
                ('registration_fee', models.CharField(default='6,000', max_length=200)),
                ('product_type', models.CharField(default='Passle, valuable', max_length=200)),
                ('dispatch_mode', models.CharField(default='Express', max_length=200)),
                ('weight', models.CharField(default='12.6', max_length=200)),
                ('planned_delivery_date', models.CharField(default='20th March 2024', max_length=200)),
            ],
        ),
    ]
