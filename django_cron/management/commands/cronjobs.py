"""
Run the cron service (intended to be executed from a cron job)

Rsage: manage.py cronjobs
"""

import sys
import signal
from datetime import datetime

from django.conf import settings
from django.core.management.base import NoArgsCommand
import django_cron


# Exit when the command last longer than CRON_TIMEOUT, if it's set
if getattr(settings, 'CRON_TIMEOUT', False):
    def timeout_check(signum, stack):
        print('Timeout, exiting!')
        sys.exit()
    
    signal.signal(signal.SIGALRM, timeout_check)
    signal.alarm(settings.CRON_TIMEOUT)


class Command(NoArgsCommand):
    help = "run the cron services (intended to be executed from a cron job)"

    def handle_noargs(self, **options):
        django_cron.autodiscover(start_timer=False, registering=False)
        print("%s: Cronjobs for %s finished" % (datetime.now(), settings.SITE_NAME))
