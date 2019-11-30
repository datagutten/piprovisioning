import os
from setuptools import find_packages, setup

# allow setup.py to be run from any path
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

setup(
    name='piprovisioning',
    version='0.1',
    packages=find_packages(),
    include_package_data=True,
    license='GPL',
    description='A django app to prepare network boot images for Raspberry Pi devices',
    url='https://github.com/datagutten/piprovisioning',
    author='Anders Birkenes',
    author_email='datagutten@datagutten.net',
    classifiers=[
        'Environment :: Web Environment',
        'Framework :: Django',
        'Framework :: Django :: 2.1',
        'Intended Audience :: System Administrators',
        'License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
    ], install_requires=['django', 'pimanager', 'requests']
)
