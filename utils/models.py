from urllib import parse
from django.db import models
from django.conf import settings
from django.utils.translation import ugettext_lazy as _
from django.utils.timezone import now as timezone_now



class UrlMixin(models.Model):
    """
    A replacement for get_absolute_url()
    Models extending this mixin should have
    either get_url or get_url_path implemented.
    """

    class Meta:
        abstract = True

    def get_url(self):
        if hasattr(self.get_url_path, 'dont_recurse'):
            raise NotImplementedError
        try:
            path = self.get_url_path()
        except NotImplementedError:
            raise
        website = getattr(settings, "DEFAULT_WEBSITE_URL",
                          "http://127.0.0.1:8000")
        return website_url + path

    get_url.dont_recurse = True

    def get_url_path(self):
        if hasattr(self.get_url, "dont_recurse"):
            raise NotImplementedError
        try:
            url = self.get_url()
        except NotImplementedError:
            raise
        bits = parse.urlparse(url)
        return parse.urlunparse(("", "") + bits[2:])

    get_url_path.dont_recurse = True

    def get_absolute_url(self):
        return self.get_url_path()


class CreationModificationDateMixin(models.Model):
    """
    Abstract base class with a creation and modification
    date and time
    """

    class Meta:
        abstract = True

    created = models.DateTimeField(
        _('create date and time'), editable=False, auto_now_add=True)

    updated = models.DateTimeField(
        _('modification date and time'),
        null=True,
        editable=False,
        auto_now=True, )
