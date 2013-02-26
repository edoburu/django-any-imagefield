"""
Custom model fields to link to CMS content.
"""
from django.conf import settings


# Include the imagefield.
if 'filebrowser' in settings.INSTALLED_APPS:
    from .backends import filebrowser as active_backend
elif 'sorl.thumbnail' in settings.INSTALLED_APPS:
    from .backends import sorl as active_backend
elif 'any_imagefield' in settings.INSTALLED_APPS:
    # Can use template-based previews
    from .backends import preview as active_backend
else:
    # Can't use template based either, use Plain old Django fields
    from .backends import default as active_backend


# This is included for documentation, consistent south migrations and editor code completion:
class AnyFileField(active_backend.AnyFileField):
    """
    The file browse field based on django-filebrowser, or any other filebrowser.
    It's a drop-in replacement for the django :class:`~django.db.models.FileField`

    When *django-filebrowser* is not installed, it will display the
    standard :class:`~django.db.models.FileField`.
    """


class AnyImageField(active_backend.AnyImageField):
    """
    The image field based on django-filebrowser, SORL thumbnail or any other image library.
    It's a drop-in replacement for the django :class:`~django.db.models.ImageField`

    When *django-filebrowser* is not installed, it will display the
    standard :class:`~django.db.models.ImageField` with a preview attached to it.
    """
    def __init__(self, *args, **kwargs):
        # django-filebrowser has no concept of a 'width_field',
        # only Django's ImageField has this feature.
        if 'width_field' in kwargs:
            raise NotImplementedError("Unable to use 'width_field' in AnyImageField, not all backends support this feature.")
        if 'height_field' in kwargs:
            raise NotImplementedError("Unable to use 'height_field' in AnyImageField, not all backends support this feature.")

        super(AnyImageField, self).__init__(*args, **kwargs)



# Tell South how to create custom fields
try:
    from south.modelsinspector import add_introspection_rules
    add_introspection_rules([], [
        "^any_imagefield\.models\.fields\.AnyFileField",
        "^any_imagefield\.models\.fields\.AnyImageField",
        "^any_imagefield\.models\.fields\.backends\.([^.]+)\.AnyFileField",
        "^any_imagefield\.models\.fields\.backends\.([^.]+)\.AnyImageField",
    ])
except ImportError:
    pass
