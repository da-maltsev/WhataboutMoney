from setuptools import setup, find_packages

setup(
    name='stock',
    version='0.1.0',
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'Click',
        'yfinance'
    ],
    entry_points={
        'console_scripts': [
            'stock = stock.main:cli',
        ],
    },
)