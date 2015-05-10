# -*- coding: utf-8 -*-
from setuptools import setup, find_packages


setup(
    name='zipstream',
    version='1.1.0',
    description='Zipfile generator',
    author='Allan Lei',
    author_email='allanlei@helveticode.com',
    url='https://github.com/allanlei/python-zipstream',
    packages=find_packages(),
    keywords='zip streaming',
    test_suite='nose.collector',
    tests_require=['nose'],
)
