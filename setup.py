#!/usr/bin/env python
# -*- coding: utf-8 -*-
try:
    from setuptools import setup, find_packages
except ImportError:
    from ez_setup import use_setuptools
    use_setuptools()
    from setuptools import setup, find_packages


with open('README.md') as readme_file:
    readme = readme_file.read()

test_requirements = [
    "tox", "mock", "pytest"
]

setup(
    name="deployer",
    version="0.1.0",
    description="Streema deployer library",
    long_description=readme,
    author="Streema Devs",
    author_email='devel@streema.com',
    url='https://github.com/streema/deployer',
    packages=find_packages(exclude=['ez_setup', 'tests']),
    package_dir={'deployer': 'deployer'},
    include_package_data=True,
    install_requires=[
        "Fabric3>=1.11.1.post1",
        "fabtools-python>=0.19.4"
    ],
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
