from filer.fields.image import FilerImageField
from filer.fields.file import FilerFileField


class AnyFileField(FilerFileField):
    """
    The file browse field based on django-filer.
    """
    def __init__(self, *args, **kwargs):
        super().__init__()


class AnyImageField(FilerImageField):
    """
    The image browse field based on django-filer.
    """
    def __init__(self, *args, **kwargs):
        super().__init__()
