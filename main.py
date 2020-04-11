
from vespers import VespersBuilder

# TODO:
# Processing tags: <rub>, <title>, <comment>
# If priest
# Actual psalm numbers (may start from 1, 2, 3)



if __name__ == "__main__":
    vb = VespersBuilder()
    print(vb.build())
