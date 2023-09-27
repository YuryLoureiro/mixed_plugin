from django.urls import path
from netbox.views.generic import ObjectChangeLogView
from . import views
from .models import *

app_name = "managedhcp"

urlpatterns = (
    path("dhcpip/", views.DHCPIpListView.as_view(), name="dhcpip_list"),
    path("dhcpip/add/", views.DHCPIpEdit.as_view(), name="dhcpip_add"),
    path("dhcpip/edit/", views.DHCPIpBulkEditView.as_view(), name="dhcpip_bulk_edit"),
    path("dhcpip/delete/", views.DHCPIpBulkDelete.as_view(), name="dhcpip_bulk_delete"),
    path("dhcpip/<int:pk>/", views.DHCPIpView.as_view(), name="dhcpip"),
    path("dhcpip/<int:pk>/edit/", views.DHCPIpEdit.as_view(), name="dhcpip_edit"),
    path("dhcpip/<int:pk>/delete/", views.DHCPIpDelete.as_view(), name="dhcpip_delete"),
    path("dhcpip/<int:pk>/changelog/", ObjectChangeLogView.as_view(), name="dhcpip_changelog", kwargs={"model": DHCPIp}),

    path("macadd/", views.MACAddListView.as_view(), name="macadd_list"),
    path("macadd/add/", views.MACAddEdit.as_view(), name="macadd_add"),
    path("macadd/edit/", views.MACAddBulkEditView.as_view(), name="macadd_bulk_edit"),
    path("macadd/delete/", views.MACAddBulkDelete.as_view(), name="macadd_bulk_delete"),
    path("macadd/<int:pk>/", views.MACAddView.as_view(), name="macadd"),
    path("macadd/<int:pk>/edit/", views.MACAddEdit.as_view(), name="macadd_edit"),
    path("macadd/<int:pk>/delete/", views.MACAddDelete.as_view(), name="macadd_delete"),
    path("macadd/<int:pk>/changelog/", ObjectChangeLogView.as_view(), name="macadd_changelog", kwargs={"model": MACAdd}),
)