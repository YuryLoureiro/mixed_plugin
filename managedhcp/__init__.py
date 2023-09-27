from extras.plugins import PluginConfig
from .version import __version__


class managedhcpConfig(PluginConfig):
    name = 'managedhcp'
    verbose_name = "Manager DHCP Plugin"
    description = ''
    version = __version__
    author = ''
    author_email = ''
    required_settings = []
    default_settings = {}


config = managedhcpConfig # noqa
