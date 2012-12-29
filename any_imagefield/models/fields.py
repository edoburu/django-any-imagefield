"""
Custom model fields to link to CMS content.
"""
from django.conf import settings


# Include the imagefield.
if 'filebrowser' in settings.INSTALLED_APPS:
    from .backends.filebrowser import FileBrowseField, ImageBrowseField
# Disabled because it has no sane default CSS:
#elif 'sorl.thumbnail' in settings.INSTALLED_APPS:
#    from .backends.sorl import FileBrowseField, ImageBrowseField
elif 'any_imagefield' in settings.INSTALLED_APPS:
    # Can use template-based previews
    from .backends.preview import FileBrowseField, ImageBrowseField
else:
    # Can't use template based either, use Plain old Django fields
    from .backends.default import FileBrowseField, ImageBrowseField


# This is included for documentation, consistent south migrations and editor code completion:
class FileBrowseField(FileBrowseField):
    """
    The file browse field based on django-filebrowser, or any other filebrowser.
    It's a drop-in replacement for the django :class:`~django.db.models.FileField`

    When *django-filebrowser* is not installed, it will display the
    standard :class:`~django.db.models.FileField`.
    """


class ImageBrowseField(ImageBrowseField):
    """
    The image browse field based on django-filebrowser, or any other filebrowser.
    It's a drop-in replacement for the django :class:`~django.db.models.ImageField`

    When *django-filebrowser* is not installed, it will display the
    standard :class:`~django.db.models.ImageField` with a preview attached to it.
    """


# Tell South how to create custom fields
try:
    from south.modelsinspector import add_introspection_rules
    add_introspection_rules([], [
        "^any_imagefield\.models\.fields\.FileBrowseField",
        "^any_imagefield\.models\.fields\.ImageBrowseField",
        "^any_imagefield\.models\.fields\.backends\.([^.]+)\.FileBrowseField",
        "^any_imagefield\.models\.fields\.backends\.([^.]+)\.ImageBrowseField",
    ])
except ImportError:
    pass
