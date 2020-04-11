
from vespers import VespersBuilder
from typika_module import TypikaModule

# TODO:
# Processing tags: <rub>, <title>, <comment>
# If priest
# Actual psalm numbers (may start from 1, 2, 3)
# ShotrableMixin

def traverse_props(obj, f, visited=[]):
    f(obj, obj.short)
    visited.append(id(obj))
    for child in vars(obj):
        x = getattr(obj, child)
        if x is not None and isinstance(x, TypikaModule):
            if getattr(x, "short") is not None and id(x) not in visited:
                traverse_props(x, f, visited)
    return visited

if __name__ == "__main__":
    vb = VespersBuilder(short=True, priest=False)
    print(vb.build())
    traverse_props(vb, print)
    print("\n\n")
    vb.short = False
    print(traverse_props(vb, print))
