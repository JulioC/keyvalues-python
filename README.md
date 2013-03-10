KeyValues.py
============

Module for parsing, using and writing files with Key Values format used by Valve.

The parser is supposed to follow the format specification, which is reproduced on [this Valve Developer Wiki page](https://developer.valvesoftware.com/wiki/KeyValues). The exception is for macros (eg `#base`, `#include`).

The KeyValues class has an interface compatible with Python dictionaries, with addition to the load(filename) and save(filename) methods.

## Installation

The package can be installed with [pip](http://www.pip-installer.org/en/latest/):

    $ pip install keyvalues

Or, for the latest version, cloning the repository and running (require setuptools):

    $ python setup.py install

## License

The KeyValues format is copyright for Valve Corporation.

All code is licensed under MIT License.