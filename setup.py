import os
from setuptools import setup, find_packages
from distutils.util import convert_path

# Define paths and placeholders.
ver_dict = {}
VER_PATH = convert_path('resnet/_version.py')
README_PATH = 'README.md'

# Read the README contents.
with open (README_PATH, 'r') as readme_file:
    README = readme_file.read()

# Read the version info.
with open(VER_PATH, 'r') as ver_file:
    exec(ver_file.read(), ver_dict)

NAME = 'resnet'
VERSION = ver_dict['__version__']  # update in resnet/_version.py!
DESCRIPTION = 'Residual networks implementation using Keras-1.0 functional API.'
LONG_DESCRIPTION_CONTENT_TYPE = 'text/markdown'
URL = 'https://github.com/raghakot/keras-resnet'
AUTHOR = 'Raghavendra Kotikalapudi'
AUTHOR_EMAIL = 'ragha@outlook.com'
LICENSE = 'MIT'
CLASSIFIERS = ['Development Status :: 5 - Production/Stable',
               'Environment :: Console',
               'Intended Audience :: Developers',
               'Intended Audience :: Science/Research',
               'License :: OSI Approved :: MIT License',
               'Natural Language :: English',
               'Operating System :: OS Independent',
               'Programming Language :: Python',
               'Programming Language :: Python :: 3',
               'Programming Language :: Python :: 3.3',
               'Programming Language :: Python :: 3.4',
               'Programming Language :: Python :: 3.5',
               'Programming Language :: Python :: 3.6',
               'Programming Language :: Python :: 3.7',
               'Topic :: Scientific/Engineering',
               'Topic :: Utilities']
KEYWORDS = 'resnet keras tensorflow theano'
PROJECT_URLS = {'Documentation': 'https://github.com/raghakot/keras-resnet',
                'Source': 'https://github.com/raghakot/keras-resnet',
                'Tracker': 'https://github.com/raghakot/keras-resnet/issues'}
PACKAGES = find_packages(exclude=['contrib', 'docs', 'tests*'])
INSTALL_REQUIRES = ['keras']

setup(name=NAME,
      version=VERSION,
      description=DESCRIPTION,
      long_description=README,
      long_description_content_type=LONG_DESCRIPTION_CONTENT_TYPE,
      url=URL,
      author=AUTHOR,
      author_email=AUTHOR_EMAIL,
      license=LICENSE,
      classifiers=CLASSIFIERS,
      keywords=KEYWORDS,
      project_urls=PROJECT_URLS,
      packages=PACKAGES,
      install_requires=INSTALL_REQUIRES)

# setup(setup_requires=['pbr'], pbr=True)
