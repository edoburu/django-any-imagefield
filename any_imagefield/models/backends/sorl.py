from __future__ import absolute_import
from django.db import models
from django.utils.safestring import mark_safe
from sorl.thumbnail.admin.current import AdminImageWidget
from .default import FileBrowseField  # can export as-is.

__all__ = ('FileBrowseField', 'ImageBrowseField')


class FixedAdminImageWidget(AdminImageWidget):
    # Fix the layout in the SORL AdminImageWidget
    template_with_initial = u'%(clear_template)s%(input_text)s: %(input)s'
    template_with_clear = u'<label style="width:auto; float: none; display: inline;" for="%(clear_checkbox_id)s">%(clear)s %(clear_checkbox_label)s</label><br />'

    def render(self, name, value, attrs=None):
        # Make sure the help text is displayed below the widget.
        orig_output = super(FixedAdminImageWidget, self).render(name, value, attrs)
        return mark_safe(
            orig_output \
            + u'<div style="clear: both;"></div>'
        )


class ImageBrowseField(models.ImageField):
    """
    The standard Django `~django.forms.widgets.ImageField` with a SORL thumbnail preview.
    """
    def formfield(self, **kwargs):
        kwargs['widget'] = FixedAdminImageWidget   # hard override for admin
        return super(ImageBrowseField, self).formfield(**kwargs)
