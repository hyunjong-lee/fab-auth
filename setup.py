# -*- coding: utf-8 -*-
"""fab-auth-keycloak

#### A plugin for authentication among keycloak and Azure AD.

#### Supports

- Superset

"""


_major_v = '0'
_minor_v = '1.2'


from os import path
import pathlib
import sys

import pkg_resources
from setuptools import setup, find_packages


if sys.version_info[:3] < (3, 6):
    raise RuntimeError("Python version 3.6 or later required.")


with pathlib.Path('requirements.txt').open() as rin:
    requirements = [str(req) for req in pkg_resources.parse_requirements(rin)]


setup(
    name='fab-auth-keycloak',
    version=f'{_major_v}.{_minor_v}',
    description='Flask AppBuilder Authentication plugin',
    url='https://github.com/hyunjong-lee/fab-auth-keycloak',
    author='Hyunjong Lee',
    author_email='hyunjong.lee.s@gmail.com',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: GNU Lesser General Public License v2 or later (LGPLv2+)',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
    ],
    packages=[
        'fab_auth_keycloak',
    ],
    python_requires='>=3.6',
    install_requires=requirements,
    test_suite='nose.collector',
    tests_require=['nose'],
    entry_points={},
    project_urls={
        'Source': 'https://github.com/hyunjong-lee/fab-auth-keycloak',
    },
    download_url=f'https://github.com/hyunjong-lee/fab-auth-keycloak/archive/v{_major_v}.{_minor_v}.tar.gz',
    keywords=['keycloak', 'AzureAD', 'superset'],
    license='LGPLv2+',
)
