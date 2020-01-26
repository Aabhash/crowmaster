#!/usr/bin/env python

"""The setup script."""

from setuptools import setup, find_packages
import os
from glob import glob

requirements = [ ]

test_requirements = ['pytest>=3', ]

setup(
    author="Aabhash",
    author_email='aabhashd@outlook.com',
    python_requires='>=3.5',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
        'Natural Language :: English',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
    ],
    description="AI Powered bot to converse with users.",
    install_requires=requirements,
    include_package_data=True,
    keywords='crowmaster-bot',
    name='crowmaster-bot',
    packages=find_packages('src'),
    package_dir={'': 'src'},
    py_modules=[os.path.splitext(os.path.basename(path))[0] for path in glob('src/*.py')],
    test_suite='tests',
    tests_require=test_requirements,
    url='https://github.com/aabhash/crowmaster-bot',
    version='0.1.0',
    zip_safe=False,
)

