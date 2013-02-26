from __future__ import absolute_import
from filebrowser.fields import FileBrowseField, FileObject


class PatchedFileObject(FileObject):
    @property
    def url(self):
        # The filebrowser returns a FileObject which differs from Django's FieldFile / ImageFieldFile object
        # Assign 'url' attribute for compatibility with
        return self.url_full


class CompatibleFileBrowseField(FileBrowseField):
    """
    Internal class to fix compatibility between Django's native FileField
    and django-filebrowser's FileBrowseField
    """

    def to_python(self, value):
        value = super(CompatibleFileBrowseField, self).to_python(value)
        if value.__class__ is FileObject:
            value.__class__ = PatchedFileObject
        return value


class AnyFileField(CompatibleFileBrowseField):
    """
    The file browse field based on django-filebrowser.
    """
    def __init__(self, *args, **kwargs):
        defaults = {
            'max_length': 100,  # Same as django FileField
            'format': 'Document',
            'directory': kwargs.pop('upload_to', ''),
        }

        defaults.update(kwargs)
        super(AnyFileField, self).__init__(*args, **defaults)


class AnyImageField(CompatibleFileBrowseField):
    """
    The image browse field based on django-filebrowser.
    """
    def __init__(self, *args, **kwargs):
        defaults = {
            'max_length': 100,  # Same as django ImageField
            'format': 'Image',
            'directory': kwargs.pop('upload_to', ''),
        }

        defaults.update(kwargs)
        super(AnyImageField, self).__init__(*args, **defaults)
