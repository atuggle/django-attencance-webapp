from __future__ import unicode_literals
from django.db import models
from tinymce.models import HTMLField


class EmailTemplate(models.Model):
    subject = models.CharField('Subject', max_length=100)
    body = HTMLField()
    enabled = models.BooleanField(default=True)

    def __str__(self):
        return "{0} - {1}".format(self.id, self.subject)

    class Meta:
        ordering = ['id', 'subject']