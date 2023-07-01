from setuptools import setup, find_packages

setup(
    name='ADATools',
    version='1.0.0',
    author='Daniel Schäle',
    author_email='dasc@hvl.no',
    description='Tools for ADA526',
    packages=find_packages(),
    install_requires=open('requirements.txt').readlines(),
    classifiers=[
        'Development Status :: under development',
        'Intended Audience :: Students',
        'Programming Language :: Python :: 3.8',
    ],
)
