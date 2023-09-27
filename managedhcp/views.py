from netbox.views import generic

from .models import *
from .forms import  *
from .tables import *
from .filters import *
from .forms import *

#DHCPIp
class DHCPIpListView(generic.ObjectListView):
    queryset = DHCPIp.objects.all()
    table = DHCPIpTable
    filterset = DHCPIpFilterSet
    filterset_form = DHCPIpFilterForm
    action_buttons = ('add',)

class DHCPIpView(generic.ObjectView):
    queryset = DHCPIp.objects.all()
    table = DHCPIpTable

class DHCPIpEdit(generic.ObjectEditView):
    queryset = DHCPIp.objects.all()
    form = DHCPIpForm


class DHCPIpDelete(generic.ObjectDeleteView):
    queryset = DHCPIp.objects.all()


class DHCPIpBulkDelete(generic.BulkDeleteView):
    queryset = DHCPIp.objects.all()
    table = DHCPIpTable


class DHCPIpBulkEditView(generic.BulkEditView):
    queryset = DHCPIp.objects.all()
    filterset = DHCPIpFilterSet
    table = DHCPIpTable
    form = DHCPIpBulkEditForm

#MACAdd
class MACAddListView(generic.ObjectListView):
    queryset = MACAdd.objects.all()
    table = MACAddTable
    filterset = MACAddFilterSet
    filterset_form = MACAddFilterForm
    action_buttons = ('add',)

class MACAddView(generic.ObjectView):
    queryset = MACAdd.objects.all()
    table = MACAddTable

class MACAddEdit(generic.ObjectEditView):
    queryset = MACAdd.objects.all()
    form = MACAddForm


class MACAddDelete(generic.ObjectDeleteView):
    queryset = MACAdd.objects.all()


class MACAddBulkDelete(generic.BulkDeleteView):
    queryset = MACAdd.objects.all()
    table = MACAddTable


class MACAddBulkEditView(generic.BulkEditView):
    queryset = MACAdd.objects.all()
    filterset = MACAddFilterSet
    table = MACAddTable
    form = MACAddBulkEditForm