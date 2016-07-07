# -*- coding: utf-8 -*-
# @Author: boyac
# @Date:   2016-07-07 21:34:48
# @Last Modified by:   boyac
# @Last Modified time: 2016-07-07 21:53:10

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = {
    'description': 'Return a list of suspects from transaction records',
    'author': 'Boya CHIOU',
    'url': 'N/A',
    'download_url': 'N/A',
    'author_email': 'N/A',
    'version': '0.1',
    'install_requires': ['nose'],
    'packages': ['getNAME'],
    'scripts': [],
    'name': 'getNAME'
}

setup(**config)