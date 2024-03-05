from setuptools import setup
long_description = open("README.md").read()

setup(name="nBomber",
version="0.2.0",
description="SMS BOMBING TOOL WITH HAVING 50,000 MESSAGE SENDING CAPACITY AT A TIME.",
long_description=long_description,
long_description_content_type='text/markdown',
author="CodingSangh",
url="https://github.com/CodingSangh/nBomber",
scripts=["nBomber"],
install_requires= ['certifi>=2020.6.20', 'chardet>=3.0.4', 'colorama>=0.4.3', 'idna>=2.10', 'requests>=2.24.0'],
classifiers=[
    'License :: OSI Approved :: MIT License',
    'Programming Language :: Python :: 3',
], )
