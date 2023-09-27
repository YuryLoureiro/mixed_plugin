import django_filters
from django.db.models import Q

from .models import *

class DHCPIpFilterSet(django_filters.FilterSet):
    q = django_filters.CharFilter(
        method='search',
        label='Search',
    )

    class Meta:
        model = DHCPIp
        fields = ['ip', 'description', 'type', 'mac']

    def search(self, queryset, ip, value):
        """Perform the filtered search."""
        if not value.strip():
            return queryset
        qs_filter = (
                Q(ip__icontains=value)
        )
        return queryset.filter(qs_filter)

    def type(self, queryset, type, value):
        """Perform the filtered search."""
        if not value.strip():
            return queryset
        qs_filter = (
                Q(type__icontains=value)
        )
        return queryset.filter(qs_filter)

class MACAddFilterSet(django_filters.FilterSet):
    q = django_filters.CharFilter(
        method='search',
        label='Search',
    )

    class Meta:
        model = MACAdd
        fields = ['MAC', 'description',]

    def search(self, queryset, MAC, value):
        """Perform the filtered search."""
        if not value.strip():
            return queryset
        qs_filter = (
                Q(MAC__icontains=value)
        )
        return queryset.filter(qs_filter)