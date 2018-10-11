from django.conf.urls import url

import django_cron.admin_views

urlpatterns = [
    url(r'^restart/$', django_cron.admin_views.restart),
]
