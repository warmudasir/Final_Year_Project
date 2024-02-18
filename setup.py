from setuptools import setup, find_packages

with open('app/requirements.txt') as f:
    requirements = f.read().splitlines()

setup(
    name='Health Connect',
    version='1.0.0',
    packages=find_packages(),
    install_requires=requirements,
)
