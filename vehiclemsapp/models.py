
from django.conf import settings
from django.contrib.auth import get_user_model
from django.db import models
from django.urls import reverse


class Vehicle(models.Model):

    vehicle_name = models.CharField(primary_key=True,max_length=50)
    vehicle_type = models.CharField(max_length=100, blank=False,null=False,default='')
    vehicle_price = models.FloatField()
    vehicle_brand = models.CharField(max_length=60,blank=False,null=False,default='')
    vehicle_model = models.CharField(max_length=30, blank=False, null=False, default='')
    vehicle_status = models.CharField(max_length=30, blank=False, null=False, default='')
    inventoryadmin_email = models.ForeignKey("users.CustomUser", on_delete=models.CASCADE)

    def __str__(self):
        return str(self.vehicle_name)

    class Meta:
        verbose_name = 'Vehicle'
        verbose_name_plural = 'Vehicle'

class VehicleAvailability(models.Model):

     vehicle_availabilityId = models.AutoField(auto_created=True, primary_key=True, max_length=6)
     vehicle_availabilityStatus = models.CharField(max_length=100, blank=False, null=False, default='')
     vehicle_availabilityComments = models.CharField(max_length=200, blank=False, null=False, default='')
     vehicle_name = models.ForeignKey(Vehicle, on_delete=models.CASCADE)

     def __str__(self):
        return str(self.vehicle_availabilityId)

     class Meta:
        verbose_name = 'VehicleAvailability'
        verbose_name_plural = 'VehicleAvailability'

class PurchaseOrder(models.Model):

     purchaseorder_Id = models.AutoField(auto_created=True, primary_key=True, max_length=6)
     purchaseorder_date = models.DateTimeField()
     totalnumberordered = models.IntegerField()
     purchaseorder_status = models.CharField(max_length=30, blank=False, null=False, default='')
     vehicle_name = models.ForeignKey(Vehicle, on_delete=models.CASCADE, related_name='vehicles')
     supplier_email = models.ForeignKey("users.CustomUser", on_delete=models.CASCADE)
     vehicle_availabilityId = models.ForeignKey(VehicleAvailability, on_delete=models.CASCADE)

     def __str__(self):
        return str(self.purchaseorder_Id)

     class Meta:
        verbose_name = 'PurchaseOrder'
        verbose_name_plural = 'PurchaseOrder'

class BillingOrder(models.Model):

     billingorder_Id = models.AutoField(auto_created=True, primary_key=True, max_length=6)
     billingorder_price = models.FloatField()
     billingorder_status = models.CharField(max_length=30, blank=True, null=True)
     billingorder_date = models.DateTimeField(auto_now=False, auto_now_add=False)
     purchaseorder_Id = models.ForeignKey(PurchaseOrder, on_delete=models.CASCADE)

     def __str__(self):
       return str(self.billingorder_Id)

     class Meta:
        verbose_name = 'BillingOrder'
        verbose_name_plural = 'BillingOrder'

