import collections

class KeyValues(collections.MutableMapping):
    """Class for representing Key Values objects, with container behavior.

    This class implements the tree data structure used by KeyValues, exposing
    method for acting like a python Dictionary, but keeping the key order.

    It also implements methods for representing its data as a string.
    """

    _parent = None
    _children = None

    def __init__(self, parent=None):
        self._parent = parent
        self._children = collections.OrderedDict()

    # Container interface
    def __contains__(self, key):
        return key in self._children

    # Iterable interface
    def __iter__(self):
        return iter(self._children)

    # Sized interface
    def __len__(self):
        return len(self._children)

    # Mapping interface
    def __getitem__(self, key):
        return self._children[key]

    # MutableMapping interface
    def __setitem__(self, key, value):
        self._children[key] = value

    def __delitem__(self, key):
        del self._children[key]

    # String conversion
    def __str__(self):
        return self.stringify()

    def stringify(self, identation=True, inline=False, space="\t"):
        """Returns the data as a string, with optional formating.

        The method generates a multiline indented string, in a similar format to
        that found on files. It's also able to create inline representation of
        the Key Value, without line breaks.

        Keyword arguments:
        identation -- If the result should be indented (default True)
        inline -- If the string should be returned without line breaks. Setting
        this True will override indentation to False (default False)
        space -- String used to indentation (default "\t")
        """

        line_break = "\n"
        if inline:
            identation = False
            line_break = ""

        if not identation:
            space = ""

        return_str = "{" + line_break
        return_str += self._stringify_recursive(identation, line_break, space, 1)
        return_str += "}"

        return return_str

    def _stringify_recursive(self, identation, line_break, space, indentation_level):
        prefix = space * indentation_level

        return_str = ""
        for key in self._children:
            return_str += prefix + '"' + str(key) + '" '

            value = self._children[key]
            if isinstance(value, KeyValues):
                return_str += "{" + line_break
                return_str += value._stringify_recursive(identation, line_break, space, indentation_level + 1)
                return_str += prefix + "}"
            else:
                return_str += '"' + str(value) + '"'

            return_str += line_break

        return return_str




if __name__ == '__main__':
    kv = KeyValues()

    kv["name"] = "Test Model"
    print("kv[\"name\"] = {}".format(kv["name"]))
    kv["filename"] = "test.mdl"
    print("kv[\"filename\"] = {}".format(kv["filename"]))

    print("len(kv) = {}".format(len(kv)))

    print("\"name\" in kv = {}".format("name" in kv))
    print("\"uncontained_key\" in kv = {}".format("uncontained_key" in kv))

    del kv["name"]
    print("Deleted kv[\"name\"]")

    print("kv items:")
    for key in kv:
        print("  kv[{0}] = {1}".format(key, kv[key]))

    print("\"name\" in kv = {}".format("name" in kv))


    kv_a = KeyValues()
    kv_a["name"] = "kv_a"

    kv_b = KeyValues()
    kv_b["name"] = "kv_b"
    kv_a["entry"] = kv_b

    kv_c = KeyValues()
    kv_c["name"] = "kv_c"
    kv_b["another"] = kv_c

    print(str(kv_a))