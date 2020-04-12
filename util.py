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

def traverse_props(obj, f, class_, attr_name, visited):
    f(obj, getattr(obj, attr_name))
    visited.append(id(obj))
    for child in vars(obj):
        x = getattr(obj, child)
        if x is not None and isinstance(x, class_):
            if getattr(x, attr_name) is not None and id(x) not in visited:
                traverse_props(x, f, class_, attr_name, visited)
    return visited
