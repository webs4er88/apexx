from django.db import models
from datetime import datetime, date



class Parcel(models.Model):
    tracking_number = models.CharField(max_length=200, unique=True, default="Track")
    delivery_progress = models.CharField(max_length=200,default="25")
    from_location = models.CharField(max_length=200,default="1745 Bassel Street Reserve, LA 70084")
    to_location = models.CharField(max_length=200,default="4509 Beechwood Avenue Cedar Knolls, NJ 07927")
    statuscolor = models.CharField(max_length=200,default="green")
    shipment_status = models.CharField(max_length=200,default="ON TRANSIT")
    current_location = models.CharField(max_length=200,default="AIRPORT CALIFORNIA, BAYWATCH OTC 123")
    agent_phone = models.CharField(max_length=200,default="+1 533 363 2735" )

    sender_name = models.CharField(max_length=200,default="NGUC CHIA")
    sender_location = models.CharField(max_length=200,default="FRANKFURT, GERMANY")
    service_type = models.CharField(max_length=200, default="AIR FREIGHT")


    recipient_name = models.CharField(max_length=200,default="JAMES V HENSFORD")
    recipient_number = models.CharField(max_length=200,default="+1 625 737 328")
    recipient_location = models.CharField(max_length=200,default="1745 Bassel Street Reserve, LA 70084")

    registration_fee = models.CharField(max_length=200,default="6,000" )
    product_type = models.CharField(max_length=200,default="Passle, valuable")
    dispatch_mode = models.CharField(max_length=200, default="Express")
    
    
    weight = models.CharField(max_length=200, default="12.6")
    Arrivaldate = models.CharField(max_length=200, default="March 2, 2024")
    planned_delivery_date = models.CharField(max_length=200, default="leave void")

    def __str__(self):
        return self.tracking_number
