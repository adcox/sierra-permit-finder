"""
Project setup
"""
from setuptools import setup

setup(
    name = 'sierra-permits',
    version = '0.0.1',
    description = 'A tool to find permits across the Sierra Nevada',
    url = 'https://github.com/adcox/sierra-permit-finder',
    author = 'Andrew Cox',
    author_email = '',
    license = '',
    packages = [
        'sierra_permits'
    ],
    install_requires = [
        'cryptography>=35.0',
        'selenium',
        #'beautifulsoup4'
    ],
    classifiers = [
        ''
    ],
)
