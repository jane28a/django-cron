"""
Run the cron service (intended to be executed from a cron job)

usage: manage.py cronjobs
"""

from django.core.management.base import BaseCommand
from django_cron.models import Cron


class Command(BaseCommand):
    help = "reset the django cron status"

    def handle(self, **options):
        print('Django Cron status reset')
        status, created = Cron.objects.get_or_create(pk=1)
        status.executing = False
        status.save()
        print('Done')