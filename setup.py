#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os.path

try:
    from setuptools import setup, find_packages
except ImportError:
    from ez_setup import use_setuptools
    use_setuptools()
    from setuptools import setup, find_packages

from pip.req import parse_requirements


with open('README.md') as readme_file:
    readme = readme_file.read()

test_requirements = [
    "tox", "mock", "pytest"
]

# parse_requirements() returns generator of pip.req.InstallRequirement objects
install_reqs = parse_requirements(os.path.join(os.path.dirname(__file__), "requirements.txt"), session=False)

setup(
    name="deployer",
    version="1.0.1",
    description="Streema deployer library",
    long_description=readme,
    author="Streema Devs",
    author_email='devel@streema.com',
    url='https://github.com/streema/deployer',
    packages=find_packages(exclude=['ez_setup', 'tests']),
    package_dir={'deployer': 'deployer'},
    include_package_data=True,
    install_requires=[str(ir.req) for ir in install_reqs],
    zip_safe=False,
    keywords='{{ cookiecutter.project_slug }}',
    classifiers=[
        'Development Status :: 1 - Stable',
        'Intended Audience :: Developers',
        'Natural Language :: English',
        "Programming Language :: Python :: 2",
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
    ],
    test_suite='tests',
    tests_require=test_requirements
)
