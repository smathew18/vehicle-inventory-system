from django.urls import path
from . import views
from .views import (
    VehicleListView,
    VehicleEditView,
    VehicleDeleteView,
    VehicleCreateView,
    VehicleAvailabilityListView,
    VehicleAvailabilityEditView,
    VehicleAvailabilityDeleteView,
    VehicleAvailabilityCreateView,
    PurchaseOrderListView,
    PurchaseOrderEditView,
    PurchaseOrderDeleteView,
    PurchaseOrderCreateView,
    BillingOrderListView,
    BillingOrderEditView,
    BillingOrderDeleteView,
    BillingOrderCreateView,
)


urlpatterns = [

    path('vehicle/<str:pk>/edit/',VehicleEditView.as_view(), name='vehicle_edit'),
    path('vehicle/<str:pk>/delete/',VehicleDeleteView.as_view(), name='vehicle_delete'),
    path('vehicle/vehiclenew/', VehicleCreateView.as_view(), name='vehicle_add'),
    path('vehiclelist/', VehicleListView.as_view(), name='vehicle_list'),
    path('vehicleavail/<int:pk>/edit/',VehicleAvailabilityEditView.as_view(), name='vehicleavail_edit'),
    path('vehicleavail/<int:pk>/delete/',VehicleAvailabilityDeleteView.as_view(), name='vehicleavail_delete'),
    path('vehicleavail/vehicleavailnew/', VehicleAvailabilityCreateView.as_view(), name='vehicleavail_add'),
    path('vehicleavaillist/', VehicleAvailabilityListView.as_view(), name='vehicleavail_list'),
    path('purchaseorder/<int:pk>/edit/',PurchaseOrderEditView.as_view(), name='purchaseorder_edit'),
    path('purchaseorder/<int:pk>/delete/',PurchaseOrderDeleteView.as_view(), name='purchaseorder_delete'),
    path('purchaseorder/purchaseordernew/', PurchaseOrderCreateView.as_view(), name='purchaseorder_add'),
    path('purchaseorderlist/', PurchaseOrderListView.as_view(), name='purchaseorder_list'),
    path('billingorder/<int:pk>/edit/',BillingOrderEditView.as_view(), name='billingorder_edit'),
    path('billingorder/<int:pk>/delete/',BillingOrderDeleteView.as_view(), name='billingorder_delete'),
    path('billingorder/billingordernew/', BillingOrderCreateView.as_view(), name='billingorder_add'),
    path('billingorderlist/', BillingOrderListView.as_view(), name='billingorder_list'),

]