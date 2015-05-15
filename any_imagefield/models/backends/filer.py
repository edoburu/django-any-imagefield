from __future__ import absolute_import

from filer.fields.image import FilerImageField
from filer.fields.file import FilerFileField


class AnyFileField(FilerFileField):
    """
    The file browse field based on django-filer.
    """
    def __init__(self, *args, **kwargs):
        super(AnyFileField, self).__init__()


class AnyImageField(FilerImageField):
    """
    The image browse field based on django-filer.
    """
    def __init__(self, *args, **kwargs):
        super(AnyImageField, self).__init__()
