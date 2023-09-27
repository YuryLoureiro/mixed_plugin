from netbox.api.viewsets import NetBoxModelViewSet

from ..models import *
from ..filters import *
from .serializers import *

class DHCPIpViewSet(NetBoxModelViewSet):
    queryset = DHCPIp.objects.all()
    serializer_class = DHCPIpSerializer
    filterset_class = DHCPIpFilterSet

class MACAddViewSet(NetBoxModelViewSet):
    queryset = MACAdd.objects.all()
    serializer_class = MACAddSerializer
    filterset_class = MACAddFilterSet