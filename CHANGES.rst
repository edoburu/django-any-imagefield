Changes in version 0.8.1 (in development)
-----------------------------------------

* Fixed missing ``url`` property for images when using django-filebrowser-no-grappelli_ instead of Django's ``ImageField``.
  This patch is not applied for the django-filebrowser-no-grappelli-django14_ fork, which does provide an ``url`` property.
* Added warning to avoid using ``width_field`` and ``height_field`` because not all backends support those.


Version 0.8.0
-------------

Initial public release, extracted from the GitHub repository
of ``django-cmsfields`` (nowadays https://github.com/edoburu/django-any-urlfield).

* Support for django-filebrowser-no-grappelli_, which includes a preview and file selector.
* Support for SORL-thumbnail_, which includes a preview
* Support for Django's default ``ImageField``, with a preview added to it.

.. _django-filebrowser-no-grappelli: https://github.com/wardi/django-filebrowser-no-grappelli
.. _django-filebrowser-no-grappelli-django14: https://github.com/smacker/django-filebrowser-no-grappelli-django14
.. _SORL-thumbnail: https://github.com/sorl/sorl-thumbnail
