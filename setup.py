#!/usr/bin/env python
# coding=utf-8

from setuptools import setup, find_packages

setup(
  name='minimax_kata',
  version='1.0.0',
  author='James Christie',
  author_email='james.aaron.christie@gmail.com',
  url='',
  download_url='',
  description='A kata for the minimax algorithm',
  long_description='A kata for the minimax algorithm',

  packages = find_packages(),
  include_package_data = True,
  package_data = { 'minimax_kata': ['minimax_kata/*'] },
  exclude_package_data = { '': ['README.txt'] },
  
  keywords='python kata minimax',
  license='GPL',
  classifiers=['Development Status :: 5 - Production/Stable',
               'Natural Language :: English',
               'Operating System :: OS Independent',
               'Programming Language :: Python :: 3',
               'License :: OSI Approved :: GNU Library or Lesser General Public License (LGPL)',
               'License :: OSI Approved :: GNU Affero General Public License v3',
               'Topic :: Internet',
               'Topic :: Internet :: WWW/HTTP',
              ],
              
  install_requires = ['setuptools'],
)
