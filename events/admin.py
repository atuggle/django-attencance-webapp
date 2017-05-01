from django.contrib import admin
from . import models


class EventAdmin(admin.ModelAdmin):
    list_display = ['title', 'date_time', 'enabled']
    fields = ['date_time', 'title', 'enabled']


class AttendeeAdmin(admin.ModelAdmin):
    list_display = ['last_name', 'first_name', 'email', 'phone']
    fields = ['first_name', 'last_name', 'email', 'phone']


admin.site.register(models.Event, EventAdmin)
admin.site.register(models.Attendee, AttendeeAdmin)
admin.site.register(models.Attendance)

