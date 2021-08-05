from django.db import models
from django.utils.translation import gettext_lazy as _
class Diary(models.Model):
    title = models.CharField(_("title"), max_length=50)
    body = models.TextField(_("diary body"))
    created = models.DateTimeField(_("diary created date"), auto_now_add=True)
    updated = models.DateTimeField(_("diary updated date"), auto_now=True)
