import mimetypes
from django.contrib.admin.widgets import AdminFileWidget
from django.template.loader import render_to_string


class ImagePreviewWidget(AdminFileWidget):
    """
    An :class:`~django.forms.FileInput` widget that also displays a preview of the image.
    """
    template_with_initial = u'%(clear_template)s</p><p>%(input_text)s: %(input)s'

    def render(self, name, value, attrs=None):
        is_image = False
        if value:
            if hasattr(value, 'path'):
                (mime_type, encoding) = mimetypes.guess_type(value.path)
            else:
                # Try to guess mime_type from name alone, for remote FileSystems (S3, etc...)
                (mime_type, encoding) = mimetypes.guess_type(value.name)
            is_image = mime_type and mime_type.startswith('image/')

        # Render different field for replacing
        input_field = super(ImagePreviewWidget, self).render(name, value, attrs)
        if not value:
            return input_field
        else:
            return render_to_string("any_imagefield/imagepreviewwidget/update.html", {
                'value': value,
                'is_image': is_image,
                'input_field': input_field,
                'input_text': self.input_text,
            })
