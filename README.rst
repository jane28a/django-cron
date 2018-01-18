How to install django-cron
==========================

1. Put ``django_cron`` into your python path
2. Add ``django_cron`` to ``INSTALLED_APPS`` in your ``settings.py`` file
3. Add the following code to the beginning of your ``urls.py`` file (just after the imports):

   .. code-block:: python

	    import django_cron
	    django_cron.autodiscover()

4. Create a file called ``cron.py`` inside each installed app that you want to add a recurring job to. The app must be installed via the ``INSTALLED_APPS`` in your ``settings.py`` or the autodiscover will not find it.

Example `cron.py`:

.. code-block:: python

  from django_cron import cronScheduler, Job, HOUR, DAY, WEEK, MONTH

  # This is a function I wrote to check a feedback email address
  # and add it to our database. Replace with your own imports
  from MyMailFunctions import check_feedback_mailbox

  class CheckMail(Job):
	"""
	Cron Job that checks the lgr users mailbox and adds any 
	approved senders' attachments to the db
	"""

	# run every hours
	run_every = HOUR
		
	def job(self):
		# This will be executed every hour
		check_feedback_mailbox()

  cronScheduler.register(CheckMail)

Notes on andybak's fork
-----------------------

- Feature: Run via normal system cron using a management command rather than the original request based triggering. Makes it usable on low-traffic sites where there might not be enough requests to reliably run your cron jobs.
- Feature: Changed time units for run_every to be minutes rather than seconds. This makes the numbers a bit less unwieldy and I couldn't see a need for the higher resolution
- Feature: Added some convenient time constants: HOUR, DAY, WEEK, MONTH (last one is actually 52/12 weeks)
- Feature: Email notifications of exceptions while running a job.
- Feature: Admin messages to all staff when jobs fail.
- Feature: Allow restarting jobs via a GET to [admin_url]/cron/restart/ (I know... I know... GET's shouldn't do this...)
- Feature: Support notifications and restarting jobs via the app django-admin-notifications if jobs have missed their schedule.
- Fixed: Registering jobs used to also run them - this tends to block the dev server if there are any long processes like a backup. Added a argument 'registering=False' to the method execute().

Extra installation steps
~~~~~~~~~~~~~~~~~~~~~~~~

1. Add an entry to your crontab. I use:

   .. code-block:: bash

	  \*/1 \* \* \* \* /path/to/python /path/to/manage.py cronjobs >> $HOME/cron.log 2>>cron_error.log

   (If you do ``PYTHONPATH`` wrangling in your ``.bash_profile`` then this might need moving into your manage.py or a similar wrapper script)

2. Add this to your root urls if you want to support restarting cron jobs via a GET:

   .. code-block:: python

	  url(r'^admin/cron/', include('django_cron.admin_urls')),
