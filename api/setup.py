from setuptools import find_packages, setup

setup(
    name='deploythedocs',
    version='1.0.0.dev0',
    packages=find_packages(exclude=('tests',)),
    url='',
    license='MIT',
    author='Charlie Hornsby',
    author_email='charlie.hornsby@hotmail.co.uk',
    description='',
    install_requires=['Django==1.10.6',
                      'djangorestframework==3.6.2',
                      'gunicorn==19.7.0',
                      'whitenoise==3.3.0'],
    setup_requires=['pytest-runner'],
    tests_require=['pytest',
                   'pytest-django'],
)
