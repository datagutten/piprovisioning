import subprocess
import os

tftp_path = '/srv/tftp'
nfs_path = '/home/piboot'

nfs_host = '10.0.4.12'


def provision(serial):
    pattern = 's=++nfs_root++=%s:%s/%s=' % (nfs_host, nfs_path, serial)
    print(pattern)
    if not os.path.exists(tftp_path + '/template'):
        raise ValueError('tftp template not found')
    if not os.path.exists(nfs_path + '/template'):
        raise ValueError('nfs template not found')

    print(subprocess.call(['rsync', '-av', tftp_path + '/template/', tftp_path + '/' + serial]))
    print(subprocess.call(['rsync', '-av', nfs_path + '/template/', nfs_path + '/' + serial]))
    print(subprocess.call(['sed', '-i', pattern,
                           tftp_path + '/' + serial + '/cmdline.txt']))
