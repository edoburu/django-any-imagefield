#!/usr/bin/env python
from setuptools import setup, find_packages
from os.path import dirname, join


setup(
    name='django-any-imagefield',
    version='0.8.1',
    license='Apache License, Version 2.0',

    requires=[
        'Django (>=1.3)',   # Using staticfiles
    ],
    extras_require = {
        'filebrowser': ['django-filebrowser'],
    },
    dependency_links = [
        'git+https://github.com/smacker/django-filebrowser-no-grappelli-django14#egg=django-filebrowser',
    ],

    description='A switchable ImageField for third party Django applications',
    long_description=open(join(dirname(__file__), 'README.rst')).read(),

    author='Diederik van der Boor',
    author_email='opensource@edoburu.nl',

    url='https://github.com/edoburu/django-any-imagefield',
    download_url='https://github.com/edoburu/django-any-imagefield/zipball/master',

    packages=find_packages(exclude=('example*',)),
    include_package_data=True,

    zip_safe=False,
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Apache Software License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ]
)
