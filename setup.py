#!/usr/bin/env python3
from distutils.core import setup
import os

PROJECT = 'phrasenoia'
VERSION = '0.2'
URL     = 'https://github.com/chrishiestand/phrasenoia'
AUTHOR  = 'Chris Hiestand'
DESC    = "passphrase generator based on diceware"
LICENSE = """
            Copyright (c) 2013 Chris Hiestand <https://github.com/chrishiestand>

            This program is free software: you can redistribute it and/or modify
            it under the terms of the GNU General Public License as published by
            the Free Software Foundation, either version 3 of the License, or
            (at your option) any later version.

            This program is distributed in the hope that it will be useful,
            but WITHOUT ANY WARRANTY; without even the implied warranty of
            MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
            GNU General Public License for more details.

            You should have received a copy of the GNU General Public License
            along with this program.  If not, see <http://www.gnu.org/licenses/>.
          """


def read_file(file_name):
    file_path = os.path.join(
        os.path.dirname(__file__),
        file_name
        )
    return open(file_path).read()

setup(name='phrasenoia',
      version          = VERSION,
      description      = DESC,
      long_description = read_file('README.md'),
      author           = AUTHOR,
      author_email     = 'chrishiestand@gmail.com',
      url              = URL,
      license          = LICENSE,
      py_modules       = ['phrasenoia'],
      data_files       = [('wordlists', ['diceware.txt'])],
      scripts          = ['scripts/passphrasegen'],
      classifiers      = [
                          'Development Status :: 3 - Alpha',
                          'Environment :: Console',
                          'Intended Audience :: End Users/Desktop',
                          'Intended Audience :: Information Technology',
                          'Intended Audience :: System Administrators',
                          'License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)',
                          'Programming Language :: Python',
                          'Programming Language :: Python :: 3',
                          'Operating System :: Unix',
                          'Topic :: Security',
                          'Topic :: Security :: Cryptography',
                          'Topic :: Software Development :: Libraries :: Python Modules',
                          'Topic :: Utilities'
                         ]
     )