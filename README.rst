django-any-imagefield
=====================

This module offers a abstraction over the various image fields,
so allow third party applications can provide an imagefield at the project choice.

Supported image fields:

* django-filebrowser-no-grappelli_, which includes a preview and file selector.
* django-filer_, which includes a preview and file selector.
* SORL-thumbnail_, which includes a preview
* Django's default ``ImageField``, with a preview added to it.


Installation
============

First install the module, preferably in a virtual environment. It can be installed from PyPI::

    pip install django-any-imagefield

Configuration
-------------

Add the module to the installed apps:

.. code-block:: python

    INSTALLED_APPS += (
        'any_imagefield',
    )

Usage
-----

In a Django model, the field can be included:

.. code-block:: python

    from django.db import models
    from any_imagefield.models import AnyImageField

    class Article(models.Model):
        title = models.CharField("Title", max_length=200)
        image = AnyImageField("Image", upload_to='images')

        class Meta:
            verbose_name = "Article"
            verbose_name_plural = "Articles"

        def __unicode__(self):
            return self.title

By default, the ``AnyImageField`` displays a standard ``ImageField`` with a preview thumbnail.
When django-filebrowser-no-grappelli_ is installed, it will use the ``FileBrowseField`` from
that package to display the file/image browser. When your package has it's own ``ImageField`` variant/subclass,
please consider to add support for it in this package.


Contributing
------------

This module is designed to be generic. In case there is anything you didn't like about it,
or think it's not flexible enough, please let us know. We'd love to improve it!

If you have any other valuable contribution, suggestion or idea,
please let us know as well because we will look into it.
Pull requests are welcome too. :-)


.. _django-filebrowser-no-grappelli: https://github.com/smacker/django-filebrowser-no-grappelli
.. _django-filer: https://github.com/stefanfoulis/django-filer
.. _SORL-thumbnail: https://github.com/sorl/sorl-thumbnail
