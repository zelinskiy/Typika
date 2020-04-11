import collections

def load(path, encoding="utf-8"):
    f = open(path, "r", encoding=encoding)
    res = f.read()
    f.close()
    return res

def flatten(l):
    for el in l:
        if isinstance(el, collections.Iterable) and not isinstance(el, (str, bytes)):
            yield from flatten(el)
        else:
            yield el
