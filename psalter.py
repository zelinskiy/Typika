from common import Common
from util import *

# notice the cathisma 17
KATHISMATA = {
    1: [[1, 2, 3],
        [4, 5, 6],
        [7, 8]],
    2: [[9, 10],
        [11, 12, 13],
        [14, 15, 16]],
    3: [[17],
        [18, 19, 20],
        [21,22,23]],
    4: [[24,25,26],
        [27,28,29],
        [30,31]],
    5: [[32,33],
        [34,35],
        [36]],
    6: [[37,38,39],
        [40,41,42],
        [43,44,45]],
    7: [[46,47,48],
        [49,50],
        [51,52,53,54]],
    8: [[55,56,57],
        [58,59,60],
        [61,62,63]],
    9: [[64,65,66],
        [67],
        [68,69]],
    10: [[70,71],
        [72,73],
        [74,75,76]],
    11: [[77],
        [78,79,80],
        [81,82,83,84]],
    12: [[85,86,87],
        [88],
        [89,90]],
    13: [[91,92,93],
        [94,95,96],
        [97,98,99,100]],
    14: [[101,102],
        [103],
        [104]],
    15: [[105],
        [106],
        [107,108]],
    16: [[109,110,111],
        [112,113,114],
        [115,116,117]],
    17: [range(1, 73),
        range(73, 132),
        range(132, 176)],
    18: [[119, 120, 121, 122, 123],
        [124, 125, 126, 127, 128],
        [129, 130, 131, 132, 133]],
    19: [[134,135,136],
        [137,138,139],
        [140,141,142]],
    20: [[143,144],
        [145,146,147],
        [148,149,150]]
}


def test_schemata():
    res = [118]
    for k in KATHISMATA:
        if k != 17:
            for glory in KATHISMATA[k]:
                for ps in glory:
                    res.append(ps)
    for i in range(1, 151):
        if i not in res:
            print("Missing " + str(i))
            return False
    return True


class Psalter:

    def __init__(self, short=False, show_numbers=False):
        self.common = Common(short=short)
        self.show_numbers = show_numbers
        self._psalms = []
        for i in range(1, 151):
            psalm = load("texts/slav/psalter/" + str(i) + ".txt")
            psalm = psalm.split("\n")
            self._psalms.append(psalm)

    def psalm_title(self, n):
        return "Psalm " + str(n)

    def psalm(self, n):
        res = [self.psalm_title(n)]
        for verse in self._psalms[n + 1]:
            res.append(verse)
        return "\n".join(res)

    def verse(self, pnum, n):
        return self._psalms[pnum + 1][n]

    def stasis(self):
        return [
            self.common.glory_and_now(),
            self.common.alleluia(),
            self.common.kyrie_eleison_3(),
            self.common.glory_and_now(),
        ]

    def kathisma(self, n):
        res = []
        kathisma = KATHISMATA[n]
        if n == 17:
            res.append(self.psalm_title(118))
            for vnum in kathisma:
                res.append("\n".join(self.verse(118, vnum)))
            res.append(self.stasis())
        else:
            for glory in kathisma:
                for pnum in glory:
                    res.append(self.psalm(pnum))
                res.append(self.stasis())
        return res
