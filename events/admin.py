from django.contrib import admin
from . import models


class EventAdmin(admin.ModelAdmin):
    list_display = ['title', 'date_time', 'enabled']
    fields = ['date_time', 'title', 'enabled']
    search_fields = ['title', 'date_time', 'enabled']
    list_filter = ['date_time', 'enabled']


class AttendeeAdmin(admin.ModelAdmin):
    list_display = ['last_name', 'first_name', 'email', 'phone']
    fields = ['first_name', 'last_name', 'email', 'phone']
    search_fields = ['last_name', 'first_name', 'email', 'phone']


class AttendanceAdmin(admin.ModelAdmin):
    list_display = ['event_id', 'event_title', 'attendee_first_name', 'attendee_last_name',
                    'attendee_email', 'attendee_phone']
    fields = ['event_title', 'attendee_first_name', 'attendee_last_name',
              'attendee_email', 'attendee_phone']
    search_fields = ['event__title', 'attendee__first_name', 'attendee__last_name',
                     'attendee__email', 'attendee__phone']
    list_filter = ['event__title']

    def event_id(self, obj):
        return obj.event.id

    def event_title(self, obj):
        return obj.event.title

    def attendee_first_name(self, obj):
        return obj.attendee.first_name

    def attendee_last_name(self, obj):
        return obj.attendee.last_name

    def attendee_email(self, obj):
        return obj.attendee.email

    def attendee_phone(self, obj):
        return obj.attendee.phone


admin.site.register(models.Event, EventAdmin)
admin.site.register(models.Attendee, AttendeeAdmin)
admin.site.register(models.Attendance, AttendanceAdmin)

