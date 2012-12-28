"""
Custom form fields for CMS items
"""
from django import forms
from .widgets import ImagePreviewWidget


class ImagePreviewField(forms.ImageField):
    """
    An `~django.forms.widgets.ImageField` subclass that also displays an inline preview of the image.
    """
    widget = ImagePreviewWidget
