
from vespers import VespersBuilder
from typika_module import TypikaModule
from util import traverse_props

# TODO:
# Processing tags: <rub>, <title>, <comment>
# If priest
# Actual psalm numbers (may start from 1, 2, 3)



if __name__ == "__main__":
    vb = VespersBuilder(short=True, priest=False)
    print(vb.build())
    traverse_props(vb, print, TypikaModule, "short", [])
    vb.set_short(False)
    print()
    traverse_props(vb, print, TypikaModule, "short", [])
