from setuptools import setup, find_packages
from io import open
from os import path

import pathlib

HERE = pathlib.Path(__file__).parent

README = (HERE / "README.md").read_text()

with open(path.join(HERE, 'requirements.txt'), encoding='utf-8') as f:
    all_reqs = f.read().split('\n')
install_requires = [x.strip() for x in all_reqs if ('git+' not in x) and (
    not x.startswith('#')) and (not x.startswith('-'))]
dependency_links = [x.strip().replace('git+', '') for x in all_reqs if 'git+' not in x]

setup(
    name='stock',
    version='0.2.0',
    packages=find_packages(),
    include_package_data=True,
    python_requires='>=3.8',
    install_requires=install_requires,
    entry_points={
        'console_scripts': [
            'stock = stock.main:entry_point',
        ],
    },
    author='Daniil Maltsev',
    long_description=README,
    long_description_content_type="text/markdown",
    license='MIT',
    url='https://github.com/da-maltsev/WhataboutMoney',
)
