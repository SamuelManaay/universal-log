from setuptools import setup

setup(
    name='universal-log',
    version='0.2',
    py_modules=['sitecustomize'],
    description='Use console.log, echo, and other logging styles globally in Python.',
    package_data={
        '': ['py.typed'],
    },
)