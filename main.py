from small_compline import SmallComplineBuilder
from vespers import VespersBuilder
from typika_module import TypikaModule
from util import traverse_props

# TODO:
# Processing tags: <rub>, <title>, <comment>
# If priest
# Actual psalm numbers (may start from 1, 2, 3)



if __name__ == "__main__":
    vb = SmallComplineBuilder(short=True, priest=False)
    print(vb.build())
