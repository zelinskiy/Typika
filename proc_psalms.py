import sys

from util import *

txt = load("texts/slav/psalms.txt")

res = []
n = 1
for ps in txt.split("\npsalm\n"):
    psalm = []
    for l in ps.split("\n\n"):
        l_ = ". ".join(l.split(". ")[1:])
        psalm.append(l_)
    res.append("\n".join(psalm))
    n += 1

if len(res) != 150:
    print("n psalms != 150")
    sys.exit(-1)


n = 1
for psalm in res:
    with open("texts/slav/psalter/" + str(n) + ".txt", "w") as f:
        f.write(psalm)
    n += 1
