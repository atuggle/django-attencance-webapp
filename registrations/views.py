from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth.decorators import login_required

from events.models import Event, Attendance


@login_required
def index(request):
    event_list = Event.objects.filter(enabled=True).order_by('-date_time')
    context = {'event_list': event_list}
    return render(request, 'registrations/index.html', context)


@login_required
def detail(request, event_id):
    event = get_object_or_404(Event, pk=event_id)
    attendance_list = Attendance.objects.filter(event=event)

    return render(request, 'registrations/detail.html', {'event': event,
                                                     'attendance_list': attendance_list})
