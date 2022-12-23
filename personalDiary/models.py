from django.db import models
from django.utils.translation import gettext_lazy as _
from django.urls import reverse
from django.contrib.auth.models import User
class Diary(models.Model):
    NORMAL = 'n'
    HAPPY = 'h'
    SAD = 's'
    MOOD_CHOICES = [
        (NORMAL, 'Normal'),
        (HAPPY, 'Happy'),
        (SAD, 'Sad')
    ]
    user = models.ForeignKey(User, verbose_name=_("User"), on_delete=models.CASCADE, null=True)
    title = models.CharField(_("title"), max_length=50)
    body = models.TextField(_("diary body"))
    mood = models.CharField(_("mood"), max_length=50, choices=MOOD_CHOICES, default=NORMAL)
    created = models.DateTimeField(_("diary created date"), auto_now_add=True)
    updated = models.DateTimeField(_("diary updated date"), auto_now=True)


    def get_absolute_url(self):
        return reverse("personalDiary:detail-diary", kwargs={"pk": self.pk})
    
    def __str__(self):
        name = 'no one' if self.user is None else self.user.username
        return f'{name} - {self.title}'

