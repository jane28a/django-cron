"""
Run the cron service (intended to be executed from a cron job)

usage: manage.py cronjobs
"""

from django.core.management.base import NoArgsCommand
from django_cron.models import Cron


class Command(NoArgsCommand):
    help = "reset the django cron status"

    def handle_noargs(self, **options):
        print('Django Cron status reset')
        status, created = Cron.objects.get_or_create(pk=1)
        status.executing = False
        status.save()
        print('Done')