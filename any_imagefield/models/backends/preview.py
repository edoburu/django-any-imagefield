from django.db import models
from .default import FileBrowseField

__all__ = ('FileBrowseField', 'ImageBrowseField')


class ImageBrowseField(models.ImageField):
    """
    The standard Django `~django.forms.widgets.ImageField` with a preview.
    """
    def formfield(self, **kwargs):
        from any_imagefield.forms.fields import ImagePreviewField
        from any_imagefield.forms.widgets import ImagePreviewWidget
        kwargs['widget'] = ImagePreviewWidget   # hard override for admin
        defaults = {'form_class': ImagePreviewField}
        defaults.update(kwargs)
        return super(ImageBrowseField, self).formfield(**defaults)
