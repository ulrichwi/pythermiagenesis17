#!/usr/bin/env python
from setuptools import setup


setup(
    name="pythermiagenesis17",
    version="0.3.0",
    author="Ulrich Wirleitner",
    author_email="ulrik@gmx.at",
    description="Python wrapper for getting data from Thermia Mega, Inverter, Calibra RXT and Stiebel Eltron WPE-I 07.1 heat pumps \
        via Modbus TCP.",
    include_package_data=True,
    url="https://github.com/ulrichwi/pythermiagenesis17",
    license="MIT",
    packages=["pythermiagenesis"],
    python_requires=">=3.6",
    install_requires=["pymodbustcp==0.1.10"],
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python",
        "Operating System :: OS Independent",
    ],
    setup_requires=("pytest-runner"),
    tests_require=(
        "asynctest",
        "pytest-cov",
        "pytest-asyncio",
        "pytest-trio",
        "pytest-tornasync",
    ),
)
