django-any-imagefield
=====================

This module offers a abstraction over the various image fields,
so allow third party applications can provide an imagefield at the authors choice.

Supported image browsers:

* django-filebrowser-no-grapelli_
* Django's default ``ImageField`` featuring a preview.
* SORL-thumbnail_ (currently disabled)


Installation
============

First install the module, preferably in a virtual environment. It can be installed from PyPI::

    pip install django-any-imagefield

Or the current folder can be installed::

    pip install .

Configuration
-------------

Next, create a project which uses the CMS::

    cd ..
    django-admin.py startproject demo

It should have the following settings::

    INSTALLED_APPS += (
        'any_imagefield',
    )

Finally, a model can use the ``AnyImageField`` field::

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

Contributing
------------

This module is designed to be generic. In case there is anything you didn't like about it,
or think it's not flexible enough, please let us know. We'd love to improve it!

If you have any other valuable contribution, suggestion or idea,
please let us know as well because we will look into it.
Pull requests are welcome too. :-)


.. _django-filebrowser-no-grapelli: https://github.com/wardi/django-filebrowser-no-grappelli
.. _SORL-thumbnail: https://github.com/sorl/sorl-thumbnail
