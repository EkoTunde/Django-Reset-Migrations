from setuptools import setup, find_packages

setup(
    name='resetmigrations',
    version="0.0.1",
    packages=find_packages(),
    install_requires=['click', 'rich'],
    entry_points='''
    [console_scripts]
    resetmigrations=resetmigrations:resetmigrations
    '''
)
