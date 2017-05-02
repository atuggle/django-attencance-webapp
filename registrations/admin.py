from django.contrib import admin
from . import models


class EmailTemplateAdmin(admin.ModelAdmin):
    list_display = ['subject', 'enabled']
    fields = ['subject', 'body', 'enabled']
    search_fields = ['subject', 'enabled']
    list_filter = ['subject', 'enabled']


admin.site.register(models.EmailTemplate, EmailTemplateAdmin)
