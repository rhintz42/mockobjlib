

class RowProxy(object):
    def __init__(self, *args, **kwargs):
        self._row = ()
        self._keys = []
        self._values = []
        self._dict = {}
        for key,val in kwargs.items():
            setattr(self, key, val)
            setattr(self, key.lower(), val)
            setattr(self, key.upper(), val)
            self._keys.append(key)
            self._row = self._row + (val,)
            self._values.append(val)
            self._dict[key] = val

    def __repr__(self):
        return str(self._row)

    def __str__(self):
        return str(self._row)

    def __getitem__(self, attr):
        return self._dict[attr]

    def __getattr__(self, attr):
        self._raise_column_error(attr)

    def keys(self):
        return self._keys

    def values(self):
        return self._values

    @property
    def __dict__(self):
        self._raise_column_error('dict')

    def _raise_column_error(self, attr):
        raise AttributeError("Could not locate column in row for column '%s'" % (attr))
