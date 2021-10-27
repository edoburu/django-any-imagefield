from django.db import models
from django.utils.safestring import mark_safe
from sorl.thumbnail.admin.current import AdminImageWidget
from .default import AnyFileField  # can export as-is.

__all__ = ('AnyFileField', 'AnyImageField')


class FixedSorlAdminImageWidget(AdminImageWidget):
    # Fix the layout in the SORL AdminImageWidget
    template_with_initial = '%(clear_template)s%(input_text)s: %(input)s'
    template_with_clear = '<span class="clearable-file-input">%(clear)s <label style="width: auto;" for="%(clear_checkbox_id)s">%(clear_checkbox_label)s</label></span><br />'

    def render(self, name, value, attrs=None, renderer=None):
        # Make sure the help text is displayed below the widget.
        orig_output = super().render(name, value, attrs, renderer=renderer)
        return mark_safe(
            orig_output \
            + '<div style="clear: both;"></div>'
        )


class AnyImageField(models.ImageField):
    """
    The standard Django `~django.forms.widgets.ImageField` with a SORL thumbnail preview.
    """
    def formfield(self, **kwargs):
        kwargs['widget'] = FixedSorlAdminImageWidget   # hard override for admin
        return super().formfield(**kwargs)
