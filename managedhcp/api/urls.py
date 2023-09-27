from rest_framework import routers
from .views import *
#app_name = 'managedhcp'

router = routers.DefaultRouter()

router.register('dhcpip', DHCPIpViewSet)
router.register('macadd', MACAddViewSet)


urlpatterns = router.urls