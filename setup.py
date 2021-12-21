from setuptools import setup, find_packages

setup(
    name='resetmigrations',
    version="0.0.2",
    packages=find_packages(),
    email='jcmacielhenning@gmail.com',
    author='Juan Cruz Maciel Henning',
    install_requires=['click', 'rich'],
    entry_points='''
    [console_scripts]
    resetmigrations=resetmigrations:resetmigrations
    '''
)
