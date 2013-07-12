#!/usr/bin/env python3
from distutils.core import setup
import os

PROJECT = 'phrasenoia'
VERSION = '0.2'
URL     = 'https://github.com/chrishiestand/phrasenoia'
AUTHOR  = 'Chris Hiestand'
DESC    = "passphrase generator based on diceware"

def read_file(file_name):
    file_path = os.path.join(
        os.path.dirname(__file__),
        file_name
        )
    return open(file_path).read()

setup(name='phrasenoia',
      version=VERSION,
      description=DESC,
      long_description=read_file('README.md'),
      author=AUTHOR,
      url=URL,
      py_modules=['phrasenoia'],
      data_files = [('wordlists', ['diceware.txt'])],
      scripts=['scripts/passphrasegen'],
      license='GPL3'
     )