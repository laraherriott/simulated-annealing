#
# pkmodel setuptools script
#
from setuptools import setup, find_packages


def get_version():
    """
    Get version number from the simulated_annealing module.
    """
    import os
    import sys

    sys.path.append(os.path.abspath('simulated_annealing'))
    from version_info import VERSION as version
    sys.path.pop()

    return version


def get_readme():
    """
    Load README.md text for use as description.
    """
    with open('README.md') as f:
        return f.read()


# Go!
setup(
    # Module name 
    name='simulated_annealing',

    # Version
    version=get_version(),

    description='A package for running simulated annealing optimization.',

    long_description=get_readme(),

    license='MIT license',

    # author='',

    # author_email='',

    maintainer='Lara Herriott',

    maintainer_email='lara.herriott@dtc.ox.ac.uk',

    url='https://github.com/laraherriott/simulated-annealing',

    # Packages to include
    packages=find_packages(include=('simulated_annealing', 'simulated_annealing.*')),

    # List of dependencies
    install_requires=[
        'numpy',
        'matplotlib',
        'scipy',
    ],
    extras_require={
        'docs': [
            # Sphinx for doc generation. Version 1.7.3 has a bug:
            'sphinx>=1.5, !=1.7.3',
            # Nice theme for docs
            'sphinx_rtd_theme',
        ],
        'dev': [
            # Flake8 for code style checking
            'flake8>=3',
        ],
    },
)