from setuptools import setup, find_packages

requires = ['argparse', 'socket']
dist = setup(
    name='Hello',
    version=__version__,
    description="print Hello",
    author="Chris McDonough",
    author_email="chrism@plope.com",
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    test_suite="supervisor.tests",
    entry_points={
        'console_scripts': [
            'hello = Hello.Hello:main'
        ],
    },
)