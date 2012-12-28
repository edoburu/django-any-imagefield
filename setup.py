#!/usr/bin/env python
from setuptools import setup, find_packages
from os.path import dirname, join


setup(
    name='django-any-imagefield',
    version='0.8.0',
    license='Apache License, Version 2.0',

    install_requires=[
        'Django',
    ],
    extras_require = {
        'filebrowser': ['django-file-browser'],
    },

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
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Apache Software License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Framework :: Django',
    ]
)
