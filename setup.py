#!/usr/bin/env python
import os
from distutils.core import setup

def read(fname):
    try:
        return open(os.path.join(os.path.dirname(__file__), fname)).read()
    except:
        return ''

setup(
    name='openssh-wrapper',
    version='0.5',
    description='OpenSSH python wrapper',
    author='Sharaf Ali',
    author_email='sharafjaffri@live.com',
    url='https://github.com/sharafjaffri/openssh-wrapper',
    long_description = read('README.rst'),
    license = 'BSD License',
    py_modules=['openssh_wrapper'],
    classifiers=(
        'Development Status :: 5 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.3',
    ),
)
