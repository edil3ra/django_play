from django.db import models
from utils.models import CreationModificationDateMixin
from utils.fields import MultilingualCharField, MultilingualTextField
from django.utils.translation import ugettext_lazy as _
from .utils import upload_to


class Note(CreationModificationDateMixin):
    title = MultilingualCharField(_('Title'), max_length=200)
    description = MultilingualTextField(_('Description'), blank=True)

    class Meta:
        verbose_name = _("Note")
        verbose_name_plural = _("Notes")

    def __str__(self):
        return self.title


class InspirationQuote(models.Model):
    author = models.CharField(verbose_name=_('Author'), max_length=200)
    quote = models.TextField(verbose_name=_('Quote'))
    picture = models.ImageField(
        _('Picture'), upload_to=upload_to, blank=True, null=True)

    class Meta:
        verbose_name = _("Inspiration Quote")
        verbose_name_plural = _("Inspiration Quotes")

    def __str__(self):
        return self.quote
