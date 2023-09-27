import django_tables2 as tables
from django_tables2.utils import A
from netbox.tables import NetBoxTable, columns
from .models import *

class DHCPIpTable(NetBoxTable):
    pk = columns.ToggleColumn()
    ip = tables.LinkColumn("plugins:managedhcp:dhcpip", args=[A("pk")], verbose_name = "IP")
    description = tables.Column(verbose_name = "Descrição")
    type = tables.Column(verbose_name = "Tipo")
    mac = tables.Column(verbose_name = "Endereço MAC")
    class Meta(NetBoxTable.Meta):
        model = DHCPIp
        fields = [
            "pk",
            "ip",
            "description",
            "type",
            "mac"
        ]

class MACAddTable(NetBoxTable):
    pk = columns.ToggleColumn()
    MAC = tables.LinkColumn("plugins:managedhcp:macadd", args=[A("pk")], verbose_name = "MAC Address")
    description = tables.Column(verbose_name = "Descrição")
    class Meta(NetBoxTable.Meta):
        model = MACAdd
        fields = [
            "pk",
            "MAC",
            "description",
        ]