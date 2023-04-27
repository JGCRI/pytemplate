import re
from setuptools import setup, find_packages


def readme():
    """Return the contents of the project README file."""

    with open('README.md') as f:
        return f.read()


version = re.search(r"__version__ = ['\"]([^'\"]*)['\"]", open('pytemplate/__init__.py').read(), re.M).group(1)

setup(
    name='pytemplate',
    version=version,
    packages=find_packages(),
    url='https://github.com/JGCRI/pytemplate',
    license='BSD-2-Clause',
    author='I.M. Human',
    author_email='i.human@machine.domain',
    description='A template for a basic Python package with CI via GitHub actions and a JOSS paper template and action',
    long_description=readme(),
    long_description_content_type="text/markdown",
    python_requires='>=3.5, <4',
    include_package_data=True,
    install_requires=[
        "pytest",
        "tqdm",
        "requests",
        "pandas>1.5",
        "numpy>=1.23",
        "PyYAML>=6",
    ],
    extras_require={
        'dev': [
            "pytest",
            "autodoc>=0.5.0",
            "twine>=4.0.1",
            "ipykernel>=6.15.1",
            "sphinx>=4.0.2",
            'sphinx-panels>=0.6.0',
            'sphinx-rtd-theme>=0.5.2',
            'sphinx-mathjax-offline>=0.0.1'
        ]
    }
)
