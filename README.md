KeyValues
=========

Module for parsing, using and writing files with Key Values format used by Valve.

The parser is supposed to follow the format specification, which is reproduced on [this Valve Developer Wiki page](https://developer.valvesoftware.com/wiki/KeyValues). The exception is for macros (eg `#base`, `#include`).

## Installation

The package can be installed with [pip](http://www.pip-installer.org/en/latest/):

    $ pip install keyvalues

Or, for the latest version, cloning the repository and running (require setuptools):

    $ python setup.py install

## Usage

For using the data structure, you can create a new instance of the KeyValues class and use its [dict](http://docs.python.org/3.3/library/stdtypes.html#mapping-types-dict) compatible interface to access and change the data values:

```python
from keyvalues import KeyValues

kv = KeyValues("kv")

kv["name"] = "Test Model"
kv["filename"] = "test.mdl"

print(str(len(kv)))

if "name" in kv:
  print("kv has name")

if "path" in kv:
  print("kv has path")

del kv["name"]

if not "name" in kv:
  print("kv doesn't have name anymore")

for key in kv:
    print("  kv[{0}] = {1}".format(key, kv[key]))
```

The class also supports loading and saving to disk:

```python
from keyvalues import KeyValues

kv = KeyValues()
kv.load("data.txt")

for key in kv:
    print("  kv[{0}] = {1}".format(key, kv[key]))

kv.save("data.txt")
```

## License

The KeyValues format is copyright for Valve Corporation.

All code is licensed under MIT License.
