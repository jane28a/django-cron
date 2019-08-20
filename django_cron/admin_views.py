from django.contrib.admin.views.decorators import staff_member_required
from django.urls import reverse
from django.http import HttpResponseRedirect


from .models import Job


@staff_member_required
def restart(request):
    for j in Job.objects.all():
        j.queued = True
        j.save()
    return HttpResponseRedirect('%s' % reverse('admin:index'))
