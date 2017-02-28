#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup

with open('README.rst') as readme_file:
    readme = readme_file.read()

with open('HISTORY.rst') as history_file:
    history = history_file.read()

requirements = [
    'click>=6.0',
    'flake8>=2.6.0',
    'Jinja2>=2.9.4',
    'pyflakes>=1.2.3',
    'PyYAML>=3.11'
]

test_requirements = [
    # TODO: put package test requirements here
]

setup(
    name='plaid',
    version='0.1.7',
    description="Python Ansible role checker",
    long_description=readme + '\n\n' + history,
    author="Scott Ison",
    author_email='sqrvrtx@gmail.com',
    url='https://github.com/sqrvrtx/plaid',
    packages=[
        'plaid',
    ],
    package_dir={'plaid':
                 'plaid'},
    entry_points={
        'console_scripts': [
            'plaid=plaid.cli:main'
        ]
    },
    include_package_data=True,
    install_requires=requirements,
    license="MIT license",
    zip_safe=False,
    keywords='plaid',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        "Programming Language :: Python :: 2",
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
    ],
    test_suite='tests',
    tests_require=test_requirements
)
