# curl -s http://pimanager/static/piprovisioning/provision_client.py|python3

import re
import socket
from uuid import getnode

import requests
from subprocess import call

# Get serial number
file = open('/proc/cpuinfo', 'r')
cpuinfo = file.read()
groups = re.search(r'Serial\s+: .*?([1-9a-f][0-9a-f]+)', cpuinfo)
if groups:
    serial = groups.group(1)
    print(serial)
else:
    raise ValueError('Serial number not found, unable to provision')


hostname = socket.gethostname()

# Register the device before provisioning starts
# https://stackoverflow.com/questions/159137/getting-mac-address
mac = getnode()
mac = ':'.join(('%012x' % mac)[i:i+2] for i in range(0, 12, 2))
response = requests.post('http://pimanager/device_status/report',
                         data={'mac': mac,
                               'hostname': hostname,
                               'serial': serial}
                         )
print(response.text)


base_url = 'http://pimanager'

url = base_url + '/provision/%s' % serial
print('Fething url %s' % url)
result = requests.get(url)
print(result.text)

call(['/sbin/reboot'])
