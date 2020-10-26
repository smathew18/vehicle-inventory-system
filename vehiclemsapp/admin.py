from django.contrib import admin

# Register your models here.
from vehiclemsapp.models import Vehicle, VehicleAvailability, PurchaseOrder, BillingOrder

class VehicleAdmin(admin.ModelAdmin):
    model = Vehicle
    list_display = ('vehicle_name','vehicle_type','vehicle_price','vehicle_brand','vehicle_model','vehicle_status')
    list_filter = ('vehicle_name','vehicle_type','vehicle_price','vehicle_brand','vehicle_model','vehicle_status')
    ordering = ['vehicle_name']

class VehicleAvailabilityAdmin(admin.ModelAdmin):
    model = VehicleAvailability
    list_display = ('vehicle_availabilityId','vehicle_availabilityStatus','vehicle_availabilityComments','vehicle_name')
    list_filter = ('vehicle_availabilityId','vehicle_availabilityStatus','vehicle_availabilityComments','vehicle_name')
    ordering = ['vehicle_name']


class PurchaseOrderAdmin(admin.ModelAdmin):
    model = PurchaseOrder
    list_display = ('purchaseorder_Id','purchaseorder_date','totalnumberordered','purchaseorder_status','vehicle_name','vehicle_availabilityId')
    list_filter = ('purchaseorder_Id','purchaseorder_date','totalnumberordered','purchaseorder_status','vehicle_name','vehicle_availabilityId')
    ordering = ['vehicle_name']

class BillingOrderAdmin(admin.ModelAdmin):
    model = BillingOrder
    list_display = ('billingorder_Id','billingorder_price','billingorder_status','billingorder_date','purchaseorder_Id')
    list_filter = ('billingorder_Id','billingorder_price','billingorder_status','billingorder_date','purchaseorder_Id')
    ordering = ['billingorder_Id']


admin.site.register(Vehicle,VehicleAdmin)
admin.site.register(VehicleAvailability,VehicleAvailabilityAdmin)
admin.site.register(PurchaseOrder,PurchaseOrderAdmin)
admin.site.register(BillingOrder,BillingOrderAdmin)
