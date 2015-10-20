import os
import sys

from setuptools import setup, find_packages
from setuptools.command.test import test as TestCommand

# Hack to prevent stupid "TypeError: 'NoneType' object is not callable" error
# in multiprocessing/util.py _exit_function when running `python
# setup.py test` or `python setup.py flake8`.  See:
#  * http://www.eby-sarna.com/pipermail/peak/2010-May/003357.html)
#  * https://github.com/getsentry/raven-python/blob/master/setup.py
import multiprocessing
assert multiprocessing  # silence flake8

version = '0.1'


def get_requirements(suffix=''):
    with open('requirements%s.txt' % suffix) as f:
        rv = f.read().splitlines()
    return rv


class PyTest(TestCommand):

    user_options = [('pytest-args=', 'a', 'Arguments to pass to py.test')]

    def initialize_options(self):
        TestCommand.initialize_options(self)
        self.pytest_args = []

    def finalize_options(self):
        TestCommand.finalize_options(self)
        self.test_args = []
        self.test_suite = True

    def run_tests(self):
        import pytest
        errno = pytest.main(self.pytest_args)
        sys.exit(errno)


def read(fname):
    """
    Utility function to read the README file.
    :rtype : String
    """
    return open(os.path.join(os.path.dirname(__file__), fname)).read()


setup(name='omero_marshal',
      version=version,
      description='OMERO Marshal',
      long_description=read('README.md'),
      classifiers=[],  # Get strings from
                       # http://pypi.python.org/pypi?%3Aaction=list_classifiers
      keywords='',
      author='Glencoe Software, Inc.',
      author_email='',
      url='https://github.com/openmicroscopy/omero-marshal',
      license='',
      packages=find_packages(),
      zip_safe=True,
      include_package_data=True,
      platforms='any',
      setup_requires=['flake8'],
      install_requires=get_requirements(),
      tests_require=get_requirements('-dev'),
      entry_points="""
      # -*- Entry points: -*-
      """,
      cmdclass={'test': PyTest},
      )
