from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect, HttpResponse

from .models import Event, Attendee, Attendance
from .forms import RegisterForm

from django.core.validators import validate_email


def index(request):
    event_list = Event.objects.filter(enabled=True).order_by('-date_time')
    context = {'event_list': event_list}
    return render(request, 'events/index.html', context)


def detail(request, event_id):
    event = get_object_or_404(Event, pk=event_id)
    if request.method == 'POST':  # if this is a POST request we need to process the form data
        form = RegisterForm(request.POST)
        if form.is_valid():
            attendee_email = update_or_create_attendee(form, event_id)
            context = {'attendee_email': attendee_email, 'event': event}
            return render(request, 'events/registration_complete.html', context)
        else:
            return render(request, 'events/detail.html', {'event': event, 'form': form})

    else:  # if a GET (or any other method) we'll create a blank form
        form = RegisterForm()
        return render(request, 'events/detail.html', {'event': event, 'form': form})

    return render(request, 'events/detail.html', {'event': event, 'form': form})


def update_or_create_attendee(form, event_id):
    form_email = form.cleaned_data['attendee_email']
    form_first_name = form.cleaned_data['attendee_first_name']
    form_last_name = form.cleaned_data['attendee_last_name']
    form_phone = form.cleaned_data['attendee_phone']
    event_attended = Event.objects.get(id=event_id)
    person = Attendee.objects.filter(email=form_email).first()

    if person is None:
        person = Attendee(first_name=form_first_name, last_name=form_last_name, email=form_email, phone=form_phone)
    else:
        person.first_name = form_first_name
        person.last_name = form_last_name
        person.phone = form_phone

    person.save()

    attendance = Attendance.objects.filter(attendee=person).filter(event=event_attended)
    if attendance is None:
        attendance = Attendance(attendee=person, event=event_attended)
        attendance.save()

    return form_email

