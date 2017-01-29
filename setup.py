# -*- coding: utf-8 -*-
import os
import sys
import codecs
from setuptools import setup, find_packages


app = __import__('bedrock')
VERSION = app.get_version()
DESCRIPTION = 'Yet another collection of seemingly essential Python features and utilities for building non-trivial applications'

def read(*files):
    return '\n'.join(
        codecs.open(os.path.join(os.path.dirname(__file__), f), 'r').read()
        for f in files    
    )

if sys.argv[-1] == 'publish':
    os.system('python setup.py sdist upload')
    sys.exit(0)


setup(
    name='bedrock',
    url='https://github.com/OpenTherapeutics/bedrock',
    author='Open Therapeutics',
    author_email='david@opentherapeutics.org',
    description=DESCRIPTION,
    version=VERSION,
    long_description=read('README.rst'),
    platforms=['any'],
    license='MIT License',
    classifiers=[
        'Environment :: OpenStack',
        'License :: OSI Approved :: MIT License',
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
        'Topic :: Utilities',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
    packages=find_packages(),
    include_package_data=True,
    package_data={'': ['*.rst'],},
    install_requires=['six'],
)
