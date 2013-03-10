__version_info__ = ('0', '1', '1')
__version__ = '.'.join(__version_info__)

from keyvalues.keyvalues import KeyValues

def load_keyvalues(filename):
    kv = KeyValues()
    kv.load(filename)
    return kv
