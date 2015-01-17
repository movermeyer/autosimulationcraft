from setuptools import setup
from sys import version_info
from autosimcraft.version import VERSION

with open('README.rst') as file:
    long_description = file.read()

requires = [
    'battlenet>=0.2.6',
    'dictdiffer>=0.3.0',
]

classifiers = [
    'Development Status :: 4 - Beta',
    'Environment :: Console',
    'Intended Audience :: End Users/Desktop',
    'License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)'
    'Natural Language :: English',
    'Operating System :: OS Independent',
    'Programming Language :: Python',
    'Programming Language :: Python :: 2',
    'Programming Language :: Python :: 2.7',
    'Programming Language :: Python :: 3',
    'Programming Language :: Python :: 3.2',
    'Programming Language :: Python :: 3.3',
    'Programming Language :: Python :: 3.4',
    'Topic :: Games/Entertainment',
]

setup(
    name='autosimcraft',
    version=VERSION,
    author='Jason Antman',
    author_email='jason@jasonantman.com',
    packages=['autosimcraft', 'autosimcraft.tests'],
    entry_points="""
    [console_scripts]
    autosimcraft = autosimcraft.runner:console_entry_point
    """,
    url='http://github.com/jantman/autosimcraft/',
    description='A python script to run SimulationCraft reports for World of Warcraft characters when their gear/stats/level/etc. changes.',
    long_description=long_description,
    install_requires=requires,
    keywords="WoW Warcraft simcraft SimulationCraft",
    classifiers=classifiers
)