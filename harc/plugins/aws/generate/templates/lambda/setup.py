from setuptools import setup, find_packages
import codecs
import os
import re

HERE = os.path.abspath(os.path.dirname(__file__))
META_PATH = os.path.join('{{project}}', '__init__.py')


def read(*parts):
    """
    Build an absolute path from *parts* and and return the contents of the
    resulting file.  Assume UTF-8 encoding.
    """
    with codecs.open(os.path.join(HERE, *parts), 'rb', 'utf-8') as f:
        return f.read()


META_FILE = read(META_PATH)


def find_meta(meta):
    """
    Extract __*meta*__ from META_FILE.
    """
    meta_match = re.search(
        r"^__{meta}__ = ['\"]([^'\"]*)['\"]".format(meta=meta),
        META_FILE, re.M
    )
    if meta_match:
        return meta_match.group(1)
    raise RuntimeError('Unable to find __{meta}__ string.'.format(meta=meta))


setup(
    name=find_meta('title'),
    version=find_meta('version'),
    description=find_meta('description'),
    long_description=read('README.md'),
    license=find_meta('license'),
    author=find_meta('author'),
    author_email=find_meta('email'),
    maintainer=find_meta('author'),
    maintainer_email=find_meta('email'),
    url=find_meta('uri'),
    classifiers=[
        # How mature is this project? Common values are
        #   3 - Alpha
        #   4 - Beta
        #   5 - Production/Stable
        'Development Status :: 3 - Alpha',

        # Indicate who your project is intended for
        # 'Intended Audience :: Other Audience',
        # 'Topic :: Other/Nonlisted Topic',
        # 'Topic :: Internet :: WWW/HTTP :: WSGI :: Middleware',
        # 'Topic :: Office/Business :: Scheduling',
        # 'Topic :: Scientific/Engineering :: Artificial Intelligence',
        # 'Topic :: Scientific/Engineering :: Information Analysis',
        # 'Topic :: Software Development :: Libraries :: Application Frameworks',
        # 'Topic :: Software Development :: Libraries :: Python Modules',

        # Pick your license as you wish (should match "license" above)
        'License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)',

        # Specify the Python versions you support here. In particular, ensure
        # that you indicate whether you support Python 2, Python 3 or both.
        # 'Programming Language :: Python :: 3',
        # 'Programming Language :: Python :: 3.6',
    ],
    keywords='development',
    packages=find_packages(exclude=['env', 'venv', 'tests', 'snippets', '{{module}}.lambdas']),
    package_data={'{{project}}': ['*.json']},
    install_requires=['boto3']
)
