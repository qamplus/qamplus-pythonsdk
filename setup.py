import sys
from os import path

from setuptools import setup, find_packages

EXCLUDE_FROM_PACKAGES = ['tests']

needs_mock = sys.version_info < (3, 3)
mock = ['mock'] if needs_mock else []

here = path.abspath(path.dirname(__file__))

version = "2.2.1"

setup(name='qamplus',
      version=version,
      description="QAMPlus SDK",
      license="MIT",
      classifiers=[
          "Development Status :: 5 - Production/Stable",
          "Intended Audience :: Developers",
          "License :: OSI Approved :: MIT License",
          "Natural Language :: English",
          "Programming Language :: Python",
          "Programming Language :: Python :: 2",
          "Programming Language :: Python :: 2.6",
          "Programming Language :: Python :: 2.7",
          "Programming Language :: Python :: 3",
          "Programming Language :: Python :: 3.3",
          "Programming Language :: Python :: 3.4",
          "Programming Language :: Python :: 3.5",
          "Programming Language :: Python :: 3.6",
      ],

      keywords='qamplus, sms, voice, mobile, emailing, api, messaging',
      author='QAMPlus Corp.',
      author_email='contact@qamplus.com',
      url="https://github.com/jeniaoo/qamplus_python",
      install_requires=['requests'],
      test_suite='nose.collector',
      tests_require=['nose', 'pytz'] + mock,
      packages=find_packages(exclude=EXCLUDE_FROM_PACKAGES),
      )