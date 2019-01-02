# -*- coding: utf-8 -*-
from setuptools import setup, find_packages


setup(
    name='enczipstream',
    version='1.1.5',
    description='Zipfile generator with password support',
    author='Allan Lei, Jonathan Koch, irma-dev',
    author_email='allanlei@helveticode.com, devthat@mailbox.org, '
                 'irma-dev@quarkslab.com',
    url='https://github.com/quarkslab/python-zipstream',
    packages=find_packages(exclude=['tests']),
    keywords='zip streaming encryption password',
    test_suite='nose.collector',
    tests_require=['nose'],
)
