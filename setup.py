import os

from setuptools import setup, find_packages

# Hack to prevent stupid "TypeError: 'NoneType' object is not callable" error
# in multiprocessing/util.py _exit_function when running `python
# setup.py test` or `python setup.py flake8`.  See:
#  * http://www.eby-sarna.com/pipermail/peak/2010-May/003357.html)
#  * https://github.com/getsentry/raven-python/blob/master/setup.py
import multiprocessing
assert multiprocessing  # silence flake8

VERSION = '0.9.0'


def get_requirements(suffix=''):
    rv = []
    with open('requirements%s.txt' % suffix) as f:
        rv = f.read().splitlines()
    return rv


def read(fname):
    """
    Utility function to read the README file.
    :rtype : String
    """
    return open(os.path.join(os.path.dirname(__file__), fname)).read()


setup(
    name='omero_marshal',
    version=VERSION,
    description='OMERO Marshal',
    long_description=read('README.rst'),
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: GNU General Public License v2 '
        'or later (GPLv2+)',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],  # Get strings from
        # http://pypi.python.org/pypi?%3Aaction=list_classifiers
    keywords='',
    author='The Open Microscopy Team, Glencoe Software, Inc.',
    author_email='ome-devel@lists.openmicroscopy.org.uk',
    url='https://github.com/ome/omero-marshal',
    license='GPLv2+',
    packages=find_packages(),
    zip_safe=True,
    include_package_data=True,
    platforms='any',
    python_requires='>=3',
    install_requires=get_requirements(),
    tests_require=get_requirements('-dev'),
    entry_points="""
    # -*- Entry points: -*-
    """,
)
