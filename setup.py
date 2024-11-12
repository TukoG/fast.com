from setuptools import setup

setup(
    name='fast',  
    version='0.1.0',
    py_modules=['fast'], 
    entry_points={  
        'console_scripts': [
            'fast=fast:main',
        ],
    },
)
