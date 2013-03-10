from keyvalues import __version__
from setuptools import setup

setup(
    name = "keyvalues",
    version = __version__,
    author = "Júlio César",
    author_email = "julio@julioc.me",
    description = ("Python implementation of Valve Key Values format."),
    keywords = "valve keyvalues",
    url = "https://github.com/JulioC/keyvalues-python",
    packages=['keyvalues'],
    classifiers=[
        "Development Status :: 3 - Alpha",
        "License :: OSI Approved :: MIT License",
    ],
    long_description="""\
    Module for parsing, using and writing files with Key Values format used by Valve.

    The parser is supposed to follow the format specification, which is reproduced
    on this Valve Developer Wiki page. The exception is for macros (eg #base, #include).

    The KeyValues class has an interface compatible with Python dictionaries, with
    addition to the load(filename) and save(filename) methods.
    """,
)