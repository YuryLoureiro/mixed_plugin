from utilities.choices import ChoiceSet

class DHCPIpTypeChoices(ChoiceSet):
    STATUS_DYNAMIC = 'dynamic'
    STATUS_STATIC = 'static'

    CHOICES = (
        (STATUS_DYNAMIC, 'Dynamic', 'blue'),
        (STATUS_STATIC, 'Static', 'yellow'),
    )