#!/usr/bin/env python
from setuptools import setup, find_packages
from os import path
import codecs
import os
import re
import sys
def read(*parts):
    file_path = path.join(path.dirname(__file__), *parts)
    return codecs.open(file_path, encoding='utf-8').read()


def find_version(*parts):
    version_file = read(*parts)
    version_match = re.search(r"^__version__ = ['\"]([^'\"]*)['\"]", version_file, re.M)
    if version_match:
        return str(version_match.group(1))
    raise RuntimeError("Unable to find version string.")


setup(
    name='django-any-imagefield',
    version=find_version('any_imagefield', '__init__.py'),
    license='Apache 2.0',

    requires=[
        'Django (>=1.3)',   # Using staticfiles
    ],
    extras_require = {
        'filebrowser': ['django-filebrowser-no-grappelli-django14'],
    },
    dependency_links = [
        'git+https://github.com/smacker/django-filebrowser-no-grappelli-django14#egg=django-filebrowser-no-grappelli-django14',
    ],

    description='A switchable ImageField for third party Django applications',
    long_description=read('README.rst'),

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
