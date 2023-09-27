
from netbox.forms import NetBoxModelForm, NetBoxModelBulkEditForm, NetBoxModelFilterSetForm  
from .models import *
from .choices import DHCPIpTypeChoices

from django import forms
from django.utils.translation import gettext as _

from utilities.forms.fields import DynamicModelChoiceField
from tenancy.models import Tenant

class DHCPIpFilterForm(NetBoxModelFilterSetForm):
    model = DHCPIp
    q = forms.CharField(
        required=False,
        label='Search'
    )
    type = forms.MultipleChoiceField(
        choices=DHCPIpTypeChoices,
        required=False
    )

class DHCPIpBulkEditForm(NetBoxModelBulkEditForm):
    pk = forms.ModelMultipleChoiceField(
        queryset=DHCPIp.objects.all(),
        widget=forms.MultipleHiddenInput
    )
    tenant = DynamicModelChoiceField(
        queryset=Tenant.objects.all(),
        required=False
    )
    description = forms.CharField(
        max_length=200,
        required=False
    )
    type = forms.ChoiceField(
        required=False,
        choices=DHCPIpTypeChoices,
    )

    model = DHCPIp
    nullable_fields = [
       'tenant', 'description',
    ]
    
class DHCPIpForm(NetBoxModelForm):
    ip = forms.CharField(
        required=True,
        label='IP'
    )
    mac = forms.CharField(
        required=True,
        label='Endereço MAC'
    )
    type = forms.ChoiceField(
        required=True,
        choices=DHCPIpTypeChoices
    )
    class Meta:
        model = DHCPIp
        fields = [
            "ip",
            "type",
            "description",
            "mac",
        ]

class MACAddFilterForm(NetBoxModelFilterSetForm):
    model = MACAdd
    q = forms.CharField(
        required=False,
        label='Search'
    )

class MACAddBulkEditForm(NetBoxModelBulkEditForm):
    pk = forms.ModelMultipleChoiceField(
        queryset=MACAdd.objects.all(),
        widget=forms.MultipleHiddenInput
    )
    tenant = DynamicModelChoiceField(
        queryset=Tenant.objects.all(),
        required=False
    )
    description = forms.CharField(
        max_length=200,
        required=False
    )

    model = MACAdd
    nullable_fields = [
       'tenant', 'description',
    ]
    
class MACAddForm(NetBoxModelForm):
    MAC = forms.CharField(
        required=True,
        label='MAC'
    )
    class Meta:
        model = MACAdd
        fields = [
            "MAC",
            "description",
        ]