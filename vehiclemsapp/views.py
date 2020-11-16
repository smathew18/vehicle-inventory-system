from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import get_object_or_404
from django.views.generic.edit import UpdateView, DeleteView, CreateView
from django.views.generic import ListView, DetailView
from .models import models
from .models import Vehicle
from .models import VehicleAvailability
from .models import PurchaseOrder
from .models import BillingOrder
from django.urls import reverse_lazy,reverse

class VehicleListView(LoginRequiredMixin,ListView):
    model = Vehicle
    template_name = 'vehicle_list.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['vehicles'] = Vehicle.objects.all()
        return context

class VehicleEditView(LoginRequiredMixin,UpdateView):
    model = Vehicle
    fields = ('vehicle_name', 'vehicle_type', 'vehicle_price', 'vehicle_brand','vehicle_model','vehicle_status')
    template_name = 'vehicle_edit.html'

    def form_valid(self, form):
        form.instance.vehicle = get_object_or_404(Vehicle, pk=self.kwargs['pk'])
        form.instance.author = self.request.user
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('vehicle_list')

class VehicleDeleteView(LoginRequiredMixin,DeleteView):
    model = Vehicle
    template_name = 'vehicle_delete.html'

    def get_success_url(self):
        return reverse('vehicle_list')

class VehicleCreateView(LoginRequiredMixin,CreateView):
    model = Vehicle
    template_name = 'vehicle_add.html'
    fields = ('vehicle_name', 'vehicle_type', 'vehicle_price', 'vehicle_brand','vehicle_model','vehicle_status','inventoryadmincontact')
    login_url = 'login'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('vehicle_list')


class VehicleAvailabilityListView(LoginRequiredMixin,ListView):
    model = VehicleAvailability
    template_name = 'vehicleavail_list.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['vehicleavails'] = VehicleAvailability.objects.all()
        return context


class VehicleAvailabilityEditView(LoginRequiredMixin,ListView):
    model = VehicleAvailability
    fields = ('vehicle_availabilityId', 'vehicle_availabilityStatus', 'vehicle_availabilityComments', 'vehicle_name')
    template_name = 'vehicleavail_edit.html'

    def form_valid(self, form):
        form.instance.vehicleavailability = get_object_or_404(VehicleAvailability, pk=self.kwargs['pk'])
        form.instance.author = self.request.user
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('vehicleavail_list')


class VehicleAvailabilityDeleteView(LoginRequiredMixin,ListView):
    model = VehicleAvailability
    template_name = 'vehicleavail_delete.html'

    def get_success_url(self):
        return reverse('vehicleavail_list')


class VehicleAvailabilityCreateView(LoginRequiredMixin,ListView):

    model = VehicleAvailability
    template_name = 'vehicleavail_add.html'
    fields = ('vehicle_availabilityId', 'vehicle_availabilityStatus', 'vehicle_availabilityComments', 'vehicle_name')
    login_url = 'login'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('vehicleavail_list')


class PurchaseOrderListView(LoginRequiredMixin,ListView):
    model = PurchaseOrder
    template_name = 'purchaserorder_list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['purchaseorders'] = PurchaseOrder.objects.all()
        return context

class PurchaseOrderEditView(LoginRequiredMixin,ListView):
    model = PurchaseOrder
    fields = ('purchaseorder_Id', 'purchaseorder_date', 'totalnumberordered', 'purchaseorder_status','vehicle_name','vehicle_availabilityId','suppliercontact')
    template_name = 'purchaserorder_edit.html'

    def form_valid(self, form):
        form.instance.purchaseorder = get_object_or_404(PurchaseOrder, pk=self.kwargs['pk'])
        form.instance.author = self.request.user
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('purchaseorder_list')


class PurchaseOrderDeleteView(LoginRequiredMixin,ListView):
    model = PurchaseOrder
    template_name = 'purchaserorder_delete.html'

    def get_success_url(self):
        return reverse('purchaseorder_list')


class PurchaseOrderCreateView(LoginRequiredMixin,ListView):
    model = PurchaseOrder
    template_name = 'purchaserorder_add.html'
    fields = ('purchaseorder_Id', 'purchaseorder_date', 'totalnumberordered', 'purchaseorder_status','vehicle_name','vehicle_availabilityId','suppliercontact')
    login_url = 'login'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('purchaseorder_list')


class BillingOrderListView(LoginRequiredMixin,ListView):
    model = BillingOrder
    template_name = 'billingorder_list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['billingorders'] = BillingOrder.objects.all()
        return context


class BillingOrderEditView(LoginRequiredMixin,ListView):
    model = BillingOrder
    fields = ('billingorder_Id', 'billingorder_price', 'billingorder_status', 'billingorder_date', 'purchaseorder_Id')
    template_name = 'billingorder_edit.html'

    def form_valid(self, form):
        form.instance.billingorder = get_object_or_404(BillingOrder, pk=self.kwargs['pk'])
        form.instance.author = self.request.user
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('billingorder_list')


class BillingOrderDeleteView(LoginRequiredMixin,ListView):
    model = BillingOrder
    template_name = 'billingorder_delete.html'

    def get_success_url(self):
        return reverse('billingorder_list')

class BillingOrderCreateView(LoginRequiredMixin,ListView):
    model = BillingOrder
    template_name = 'billingorder_add.html'
    fields = ('billingorder_Id', 'billingorder_price', 'billingorder_status', 'billingorder_date', 'purchaseorder_Id')
    login_url = 'login'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('billingorder_list')