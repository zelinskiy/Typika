from weekday import Day
import os
import shutil

# tone 0 = for all tones

def mkfile(tone, day, path):
    day_name = Day(day).name
    path_ = "texts/slav/octoechos/tone{}/{}/{}".format(tone, day_name, path)
    os.makedirs(os.path.dirname(path_), exist_ok=True)
    with open(path_, "w") as f:
        f.write(path_)

shutil.rmtree("texts/slav/octoechos/")

for tone in range(1, 9):
    for day in range(7):
        # matins
        for i in range(1, 4):
            mkfile(tone, day, "matins/kathismas/" + str(i) + ".txt")
        if day == 0:
            mkfile(tone, day, "matins/kathismas/ypakoi.txt")
            mkfile(tone, day, "matins/anabathmos.txt")
            mkfile(tone, day, "matins/prokeimenon.txt")
            mkfile(tone, day, "matins/gospel_stikhira.txt")
            mkfile(tone, day, "matins/troparion.txt")
        for i in range(1, 4):
            mkfile(tone, day, "matins/kanonA/" + str(i) + ".txt")
            mkfile(tone, day, "matins/kanonB/" + str(i) + ".txt")
            if day == 0:
                mkfile(tone, day, "matins/kanonC/" + str(i) + ".txt")
        mkfile(tone, day, "matins/stikhiras_praise.txt")

        # small and great vespers
        if day == 0:
            # small vespers
            for i in range(1, 4):
                mkfile(tone, day, "vespers/stikhiras_lord_i_cried/" + str(i) + ".txt")
            # great_vespers
            for i in range(1, 11):
                mkfile(tone, day, "great_vespers/stikhiras_lord_i_cried/" + str(i) + ".txt")
            mkfile(tone, day, "great_vespers/stikhiras_lord_i_cried/dogmatikon.txt")
            mkfile(tone, day, "great_vespers/apostikha.txt")
        else:
            for i in range(1, 7):
                mkfile(tone, day, "vespers/stikhiras_lord_i_cried/" + str(i) + ".txt")
        # all vespers
        mkfile(tone, day, "vespers/apostikha.txt")
        mkfile(tone, day, "vespers/troparion.txt")
        mkfile(tone, day, "vespers/theotokion.txt")

        # small compline
        for i in range(1, 10):
            if i == 2:
                continue
            mkfile(tone, day, "small_compline/kanon/" + str(i) + ".txt")

for day in range(7):
    mkfile(0, day, "matins/exapostilarion.txt")
