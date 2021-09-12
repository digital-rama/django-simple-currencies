import os
from setuptools import setup, find_packages


README = open(os.path.join(os.path.dirname(__file__), 'README.md')).read()

# allow setup.py to be run from any path
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

setup(
    name='django-simple-currencies-py3',
    version='1.0',
    packages=find_packages(exclude=['example']),
    include_package_data=True,
    license='BSD License',
    description='Currency, exchange rate and conversions support for django projects',
    long_description=README,
    url='https://github.com/ramananda-kairi/django-simple-currencies-py3',
    author='Ramananda Kairi',
    author_email='ramananda.kairi@gmail.com',
    install_requires=[
        'django-classy-tags',
        'openexchangerates',
    ],
    classifiers=[
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
    ],
)
