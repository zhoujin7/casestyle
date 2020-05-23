#!/usr/bin/env python
# coding=utf-8

from setuptools import setup

with open('README.rst', 'r', encoding='utf-8') as f:
    readme = f.read()

setup(
    name='casestyle',
    version='0.0.2',
    keywords=['casestyle', 'inflection', 'stringcase', 'humps', 'snake case', 'camel case', 'pascal case', 'dash case', 'const case'],
    description='String case style converter (snake_case, camelCase, PascalCase, dash-case, CONST_CASE can be converted to each other).',
    long_description=readme,
    author='zhoujin7',
    author_email='zhoujin7@foxmail.com',
    url='https://github.com/zhoujin7/casestyle',
    py_modules=['casestyle'],
    license='Apache License 2.0',
    zip_safe=False,
    python_requires='>=3',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'License :: OSI Approved :: Apache Software License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: Implementation :: CPython',
        'Programming Language :: Python :: Implementation :: PyPy',
    ]
)
