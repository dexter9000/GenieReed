# from distutils.core import setup
from setuptools import setup

setup(
    name='genie_reed',
    version='0.1.0',  # 版本号
    author='Alex',
    author_email='dexter2000@126.om',
    url='https://github.com/dexter9000/GenieReed',
    description='',
    # py_modules=['', 'es', 'gui', 'ui'],
    packages=['es', 'gui', 'ui', 'resources'],
    scripts = ['main.py'],
    install_requires=[
        'elasticsearch>=7.8.0',
        'PyQt5>=5.15.0'
    ],
    entry_points={'console_scripts': [
        'main_run = main:main',
    ]},
)
