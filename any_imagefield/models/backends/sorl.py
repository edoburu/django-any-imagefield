from __future__ import absolute_import
from django.db import models
from sorl.thumbnail.admin.current import AdminImageWidget
from .default import FileBrowseField  # can export as-is.

__all__ = ('FileBrowseField', 'ImageBrowseField')


class ImageBrowseField(models.ImageField):
    """
    The standard Django `~django.forms.widgets.ImageField` with a SORL thumbnail preview.
    """
    def formfield(self, **kwargs):
        kwargs['widget'] = AdminImageWidget   # hard override for admin
        return super(ImageBrowseField, self).formfield(**kwargs)
