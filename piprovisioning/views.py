# Create your views here.
from django.http import HttpResponse


def provision(request, serial):
    from .provision import provision
    from pimanager.models import Action
    from pimanager.models import Device
    device = Device.objects.get(serial=serial)

    try:
        provision(serial)
    except ValueError as exception:
        return HttpResponse('Unable to provision: %s' % exception)

    # Clear SSH keys on first boot
    action1 = Action(device=device, command='rm /etc/ssh/ssh_host_*')
    action1.save()
    action2 = Action(device=device, command='dpkg-reconfigure openssh-server')
    action2.save()
    action3 = Action(device=device, command='wget -O /tmp/client_setup.sh http://pimanager/static/pimanager/client_scripts/client_setup.sh')
    action3.save()
    action4 = Action(device=device, command='sh /tmp/client_setup.sh')
    action4.save()

    return HttpResponse('Provisioning for %s complete' % serial)
