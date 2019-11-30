from django.core.management.base import BaseCommand
# from django.utils import timezone

from piprovisioning.provision import provision


class Command(BaseCommand):
    help = 'Provision device'

    def add_arguments(self, parser):
        parser.add_argument('device', nargs='+', type=str)

    def handle(self, *args, **options):
        provision(options['device'][0])
