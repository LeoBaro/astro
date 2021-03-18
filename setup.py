#!/usr/bin/python
# -*- coding: latin-1 -*-
from setuptools import setup, find_packages
setup( name='astro',
       version='1.0.0',
       author='Simone Tampieri',
       author_email='simone.tampieri@inaf.it',
       packages=find_packages(),
       package_dir={ 'astro': 'astro' },
       include_package_data=True
     )