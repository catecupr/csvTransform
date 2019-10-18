from setuptools import setup

setup(
    name = 'csvTransform',
    version = '1.0.0',
    packages = ['csvTransform', 'csvTransform.Args', 'csvTransform.Transform'],
    entry_points = {
        'console_scripts': [
            'csvTransform = csvTransform.__main__:main'
        ]
    },
    install_requires= ['pandas']
)