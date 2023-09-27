from django.db import models
from django.urls import reverse
from netmiko import ConnectHandler
from utilities.querysets import RestrictedQuerySet

from .choices import *

class DHCPIp(models.Model):
    ip = models.CharField(
        max_length=200
    )
    description = models.CharField(
        max_length=200,
        blank=True
    )
    type = models.CharField(
        max_length=200,
        choices=DHCPIpTypeChoices
    )
    mac = models.CharField(
        max_length=200
    )

    objects = RestrictedQuerySet.as_manager()
    class Meta:
        app_label = "managedhcp"
        ordering = ["ip"]
        verbose_name = 'DHCPIp'
        verbose_name_plural = 'DHCPIp'

    def __str__(self):
        return self.ip

    def get_absolute_url(self):
        return reverse("plugins:managedhcp:dhcpip_list")

class MACAdd(models.Model):
    MAC = models.CharField(
        max_length=200,
        blank=False
    )
    description = models.CharField(
        max_length=200,
        blank=False
    )

    objects = RestrictedQuerySet.as_manager()
    class Meta:
        app_label = "managedhcp"
        ordering = ["MAC"]
        verbose_name = 'MACAdd'
        verbose_name_plural = 'MACAdd'

    def __str__(self):
        return self.MAC

    def get_absolute_url(self):
        return reverse("plugins:managedhcp:macadd_list")
    
    def delete(self, *args, **kwargs):
        device = ConnectHandler(device_type='huawei', ip='10.133.0.39', username='yury', password='Yury3985*')

        device.enable()
        remove_mac = 'undo sta-mac ' + self.MAC
        device.send_config_set(['wlan', 'sta-whitelist-profile name Liberados', remove_mac])

        device.disconnect()

        super().delete(*args, **kwargs)
    
    def save(self, *args, **kwargs):
        new_mac = self.pk is None
        if not new_mac:
            old_MAC = MACAdd.objects.get(pk=self.pk)

        mac_changed = not new_mac and old_MAC.MAC != self.MAC
        descripton_changed = not new_mac and old_MAC.description != self.description

        super().save(*args, **kwargs)

        if mac_changed or descripton_changed:
            for record in self.record_set.filter(
                type__in=(RecordTypeChoices.A, RecordTypeChoices.AAAA)
            ):
                record.update_ptr_record()

        self.update_soa_record()