#!/usr/bin/env python
from setuptools import find_packages, setup

setup(
    name='nameko-examples-grpc-products',
    version='0.0.1',
    description='Store and serve products',
    author='nameko',
    packages=find_packages(exclude=['test', 'test.*']),
    install_requires=[
        "marshmallow==2.15.1",
        "nameko==2.11.0",
        "redis==2.10.5",
    ],
    extras_require={
        'dev': [
            'pytest==4.3.0',
            'coverage==4.4.1',
            'flake8==3.3.0',
            "grpcio-tools",
        ]
    },
    zip_safe=True,
)
