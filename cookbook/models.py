from django.db import models
from utils.models import CreationModificationDateMixin
from utils.fields import MultilingualCharField, MultilingualTextField
from django.utils.translation import ugettext_lazy as _

class Note(CreationModificationDateMixin):
    title = MultilingualCharField(_('Title'), max_length=200)
    description = MultilingualTextField(_('Description'), blank=True)
    
    class Meta:
        verbose_name = _("Note")
        verbose_name_plural = _("Notes")
    
    def __str__(self):
        return self.title

