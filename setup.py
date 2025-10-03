from setuptools import setup

setup(
    name="vendas-cli",
    version="1.0",
    packages=['app'],
    package_dir={'app': 'app'},
    entry_points={
        'console_scripts': ['vendas-cli=app.run:main', ]
    }
)