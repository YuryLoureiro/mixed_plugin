from extras.plugins import PluginMenuButton, PluginMenuItem
from utilities.choices import ButtonColorChoices


menu_items = (
    PluginMenuItem(
        link="plugins:managedhcp:dhcpip_list",
        link_text="DHCP",
        permissions=["managedhcp.admin_full"],
        buttons=(
            PluginMenuButton(
                link='plugins:managedhcp:dhcpip_add',
                title='Add',
                icon_class='mdi mdi-plus-thick',
                color=ButtonColorChoices.GREEN,
                permissions=['managedhcp.admin_full'],
            ),
        ),
        ),
    PluginMenuItem(
        link="plugins:managedhcp:macadd_list",
        link_text="Wifi - MAC Address",
        permissions=["managedhcp.admin_full"],
        buttons=(
            PluginMenuButton(
                link='plugins:managedhcp:macadd_add',
                title='Add',
                icon_class='mdi mdi-plus-thick',
                color=ButtonColorChoices.GREEN,
                permissions=['managedhcp.admin_full'],
            ),
        ),
        ),
    )
