import sys

dependencies = ['chardet', 'jinja2', 'mock', 'nose', 'python-modargs']

if sys.platform != 'win32':
    dependencies += 'python-daemon'

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = {
    'package_data': {
        'lamson': ['data/prototype.zip']
    }, 
    'description': 'Lamson is a modern Pythonic mail server built like a web application server.',
    'author': 'Zed A. Shaw',
    'url': 'http://pypi.python.org/pypi/lamson',
    'download_url': 'http://pypi.python.org/pypi/lamson',
    'author_email': 'zedshaw@zedshaw.com',
     'version': '1.3.4',
     'scripts': ['bin/lamson'],
     'entry_points': {'console_scripts': [
             'lamson = lamson:_main'
             ]},
     'install_requires': dependencies,
     'packages': ['lamson',
     'lamson.handlers'],
     'name': 'lamson'
}

setup(**config)
