# -*- coding: utf-8 -*-

"""
Copyright (C) 2017 Zato Source s.r.o. https://zato.io

Licensed under LGPLv3, see LICENSE.txt for terms and conditions.
"""

# Part of Zato - ESB, SOA, REST, APIs and Cloud Integrations in Python
# https://zato.io

from __future__ import absolute_import, division, print_function, unicode_literals

import os, sys
from setuptools import setup, find_packages

version = '1.6'

LONG_DESCRIPTION = """"""

package_dir = b'src' if sys.version_info.major == 2 else 'src'

setup(
      name = 'zato-websocket-client',
      version = version,

      author = 'Zato Source s.r.o.',
      author_email = 'info@zato.io',
      url = 'https://zato.io/docs',
      description = 'A convenience WebSocket Python client for Zato services',
      long_description = LONG_DESCRIPTION,
      platforms = ['OS Independent'],
      license = 'GNU Lesser General Public License v3 (LGPLv3)',

      package_dir = {'':package_dir},
      packages = find_packages(package_dir),

      namespace_packages = ['zato'],
      install_requires = [
          'future',
          'gevent',
          'six',
          'ws4py',
      ],

      zip_safe = False,

      classifiers = [
        'Development Status :: 5 - Production/Stable',
        'Environment :: Console',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'Intended Audience :: Information Technology',
        'Intended Audience :: Other Audience',
        'License :: OSI Approved :: GNU Lesser General Public License v3 (LGPLv3)',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 3',
        'Intended Audience :: Developers',
        'Topic :: Communications',
        'Topic :: Education :: Testing',
        'Topic :: Internet',
        'Topic :: Internet :: Proxy Servers',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Security',
        'Topic :: System :: Networking',
        'Topic :: Utilities',
        ],
)
