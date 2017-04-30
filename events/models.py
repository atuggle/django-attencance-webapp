from __future__ import unicode_literals
from datetime import datetime
from django.utils import timezone
from django.utils.html import format_html
from django.core.validators import RegexValidator
from tinymce.models import HTMLField

from django.db import models


class Event(models.Model):
    title = models.TextField('Title', max_length=200, blank=False)
    date_time = models.DateField('Event date time', default=timezone.now)
    enabled = models.BooleanField(default=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-date_time']


class Attendee(models.Model):
    first_name = models.CharField('First Name', max_length=200)
    last_name = models.CharField('Last Name', max_length=200)
    email = models.EmailField(max_length=200)
    phone_regex = RegexValidator(regex=r'^\+?1?\d{8,15}$',
                                 message='Phone number must be entered in the format: ''+999999999''. Up to 15 digits allowed.')
    phone = models.CharField(validators=[phone_regex], blank=True,
                             max_length=16, null=True) #validators should be a list

    def __str__(self):
        return "{0} {1} - {2}".format(self.first_name, self.last_name, self.email)

    class Meta:
        verbose_name_plural = 'Attendees'


class Attendance(models.Model):
    attendee = models.ForeignKey(Attendee)
    event = models.ForeignKey(Event)

    def __str__(self):
        return "{0} : {1} was attended by {2}".format(self.event.id, self.event, self.attendee)

    class Meta:
        ordering = ['event']
