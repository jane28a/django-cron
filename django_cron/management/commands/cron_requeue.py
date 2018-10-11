"""
Requeue all the cronjobs.

Usage: ./manage.py cron_requeue
"""

from django.core.management.base import NoArgsCommand
from django_cron.models import Job


class Command(NoArgsCommand):
    help = "Set all jobs to be queued again."

    def handle_noargs(self, **options):
        print('Django Cron requeueing all jobs.')
        for job in Job.objects.all():
            job.queued = True
            job.save()
            print("Requeued ", job)
        print('Done')
