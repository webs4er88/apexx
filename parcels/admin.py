from django.contrib import admin
from .models import Parcel
#from .models import Stoppage

@admin.register(Parcel)
class ParcelAdmin(admin.ModelAdmin):
    list_display = ['tracking_number', 'weight', 'planned_delivery_date']
    search_fields = ['tracking_number', 'description']
    list_filter = ['planned_delivery_date']




# @admin.register(Stoppage)
# class StoppageAdmin(admin.ModelAdmin):
#     search_fields = ["stop_location", "stop_status","delivery_date","admin_remark" "describe_stop"]
#    # search_fields = ['tracking_number', 'description']
#     #list_filter = ['planned_delivery_date']



