from rest_framework import serializers
#from managedhcp.models import managedhcp
from ..models import *
from netbox.api.fields import ChoiceField
from netbox.api.serializers.nested import WritableNestedSerializer


class NestedDHCPIpSessionSerializer(WritableNestedSerializer):
    url = serializers.HyperlinkedIdentityField(view_name='plugins:managedhcp:dhcpip')

    class Meta:
        model = DHCPIp
        fields = ['id', 'url', 'ip', 'description']
        validators = []

class MACAddIpSessionSerializer(WritableNestedSerializer):
    url = serializers.HyperlinkedIdentityField(view_name='plugins:managedhcp:macadd')

    class Meta:
        model = MACAdd
        fields = ['id', 'url', 'MAC', 'description']
        validators = []


class DHCPIpSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    ip = serializers.CharField()
    display = serializers.SerializerMethodField('get_display')
    description = serializers.CharField()
    type = ChoiceField(choices=DHCPIpTypeChoices, required=False)
    mac = serializers.CharField()
    def get_display(self, obj):
        return f"{obj}"

    class Meta:
        model = DHCPIp
        fields = [
            'id', 'display', 'ip', 'descripton', 'type', 'mac',
        ]

    def create(self, validated_data):
        return DHCPIp.objects.create(**validated_data)

class MACAddSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    MAC = serializers.CharField()
    display = serializers.SerializerMethodField('get_display')
    description = serializers.CharField()
    def get_display(self, obj):
        return f"{obj}"

    class Meta:
        model = MACAdd
        fields = [
            'id', 'display', 'MAC', 'descripton',
        ]

    def create(self, validated_data):
        return MACAdd.objects.create(**validated_data)