from setuptools import setup, find_packages

setup(
    name='parser',
    version='1.0',
    packages=find_packages(),
    install_requires=[
        'pandas',
        'numpy'
    ],
    entry_points={
        'console_scripts': [
            'parser=main:main'
        ]
    },
    test_suite='tests',
    tests_require=[
        'pytest',
        'pytest-cov'
    ]
)
