from django.db import models
from .default import AnyFileField

__all__ = ('AnyFileField', 'AnyImageField')


class AnyImageField(models.ImageField):
    """
    The standard Django `~django.forms.widgets.ImageField` with a preview.
    """
    def formfield(self, **kwargs):
        from any_imagefield.forms.fields import ImagePreviewField
        from any_imagefield.forms.widgets import ImagePreviewWidget
        kwargs['widget'] = ImagePreviewWidget   # hard override for admin
        defaults = {'form_class': ImagePreviewField}
        defaults.update(kwargs)
        return super(AnyImageField, self).formfield(**defaults)
