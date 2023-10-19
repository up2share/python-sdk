from setuptools import setup, find_packages

with open('requirements.txt') as f:
    requirements = f.read().splitlines()

setup(
    name='u2s_sdk',
    version='0.1.0',
    description='Up2Share SDK for Python',
    author='Corentin Chepeau',
    author_email='corentin.chepeau@email.com',
    packages=find_packages(),
    install_requires=requirements,
)
