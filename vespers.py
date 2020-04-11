from common import Common
from ectenia import Ectenia
from psalter import Psalter
from typika_sign import TypikaSign
from util import *



# 2 kathismas at Matins
PSALTER_SCHEME_1 = {
    "Sat": [1],
    "Sun": [],
    "Mon": [6],
    "Tue": [9],
    "Wed": [12],
    "Thu": [15],
    "Fri": [18]
}

# 3 kathismas at Matins
PSALTER_SCHEME_2 = {
    "Sat": [],
    "Sun": [],
    "Mon": [18],
    "Tue": [18],
    "Wed": [18],
    "Thu": [18],
    "Fri": [18]
}

# lenten
PSALTER_SCHEME_3 = {
    "5": {
        "Sat": [1],
        "Sun": [],
        "Mon": [10],
        "Tue": [19],
        "Wed": [7],
        "Thu": [12],
        "Fri": [18]
    },
    # If Annunciation falls on Thursday
    "5_": {
        "Sat": [1],
        "Sun": [],
        "Mon": [11],
        "Tue": [16],
        "Wed": [],
        "Thu": [],
        "Fri": [18]
    },
    # Passion week
    "7": {
        "Sat": [1],
        "Sun": [],
        "Mon": [18],
        "Tue": [18],
        "Wed": [18],
        "Thu": [],
        "Fri": []
    },
    # weeks 1-4,6
    "default": {
        "Sat": [1],
        "Sun": [],
        "Mon": [18],
        "Tue": [18],
        "Wed": [18],
        "Thu": [18],
        "Fri": [18]
    }
}

class VespersBuilder:

    def __init__(self):
        # Heavenly King, Trisagion, Our Father, etc.
        self.short_common = False
        self.lent = False
        self.alleluia = False
        self.typika_sign = TypikaSign.Ferial
        self.priest = False
        self.common = Common()
        self.ectenia = Ectenia()
        self.psalter = Psalter()
        self.day = "Sat"

    def load(self, path):
        return load("texts/slav/horologion/vespers/" + path)

    def opening(self):
        sequence = [
            self.common.through_the_prayers_of_our_holy_fathers(),
            self.common.glory_to_thee_our_God(),
            self.common.heavenly_king(),
            self.common.trisagion(),
            self.common.glory_and_now(),
            self.common.our_father(),
            self.common.come_let_us_worship(),
        ]
        return sequence

    def psalm103(self):
        return "\n".join([
            self.psalter.psalm(103),
            self.load("103append.txt"),
            self.common.glory_and_now(),
            self.common.alleluia()
        ])

    def kathismata(self):
        if True:
            scheme = PSALTER_SCHEME_1
        elif True:
            scheme = PSALTER_SCHEME_2
        elif True:
            scheme = PSALTER_SCHEME_3

        kathismas = scheme[self.day]
        if len(kathismas) > 0:
            return list(map(self.psalter.kathisma, kathismas))
        else:
            return "NO PSALTER"

    # Стихиры на Господи, воззвах
    def stikhiras_lord_i_cried(self):
        return "LORD I CRIED STIKHIRAS"

    def theotokion(self):
        return "O joyous Light"

    def prokeimenon(self):
        if self.lent and self.alleluia:
            return "Alleluia verses"
        else:
            return "Weekday prokeimenon"

    def paremias(self):
        if self.typika_sign > TypikaSign.Polyeleos:
            return "SAINT OR FEAST PAREMIAS"
        else:
            return "NO PAREMIAS"

    # Сподоби, Господи
    def vouchsafe(self):
        return "SPODOBI"

    # Стихиры на стиховне
    def aposticha(self):
        res = "CURRENT APOSTICHA\n"
        if self.day == "Sat":
            res += "Lord reignst\n"
        if self.typika_sign > TypikaSign.Polyeleos:
            res += "Festal aposticha\n"
        return res

    # Богородичен
    def theotokion(self):
        return "Current theotokion"

    def simeon_canticle(self):
        return "Ныне отпущаеши"

    def troparion(self):
        return "Current troparion"

    def lent_troparion(self):
        return "Слава. Крестителю Христов. И ныне. Молите за ны. Под твое благоутробие."

    def lent_heavenly_king(self):
        return "Небесный Царю, православныя христианы укрепи."

    def all_holy_trinity_consubstantial_power(self):
        return "Всесвятая Троице, единосущная державо."

    def dismissal(self):
        return self.common.through_the_prayers_of_our_holy_fathers()

    def closing(self):
        if self.lent and self.alleluia:
            sequence = [
                self.common.hail_Mary(),
                self.lent_troparion(),
                self.common.kyrie_eleison_40(),
                self.common.glory_and_now(),
                self.more_honourable_cherubim(),
                # bless, father,
                self.lent_heavenly_king(),
                self.common.ephrem_prayer(),
                self.common.trisagion(),
                self.common.most_holy_trinity(),
                self.all_holy_trinity_consubstantial_power(),
                self.commons.let_lords_name_be_blessed(),
                self.commons.glory_and_now(),
                self.psalter.psalm(33),
                self.psalter.psalm(144),
                self.commons.axios_estin(),
                self.common.glory_and_now(),
                self.common.kyrie_eleison_3(),
                # bless,
                self.dismissal()
            ]
        elif self.alleluia:
            sequence = [
                "Fast non-lenten sequence"
            ]
        else:
            sequence = [
                self.troparion(),
                self.common.glory_and_now(),
                self.theotokion(),
                self.dismissal()
            ]
        return sequence




    def build(self):
        shrt = self.short_common
        sequence = [
            self.opening(),
            self.psalm103(),
            self.ectenia.great(),
            self.kathismata(),
            self.ectenia.small(),
            # self.ot_reading(),
            self.stikhiras_lord_i_cried(),
            # self.nt_reading(),
            self.common.glory_and_now(),
            self.theotokion(),
            self.prokeimenon(),
            self.paremias(),
            self.ectenia.fervent(),
            self.vouchsafe(),
            self.ectenia.vespers_supplication(),
            self.aposticha(),
            self.common.glory_and_now(),
            self.theotokion(),
            self.common.trisagion(),
            self.common.most_holy_trinity(),
            self.common.our_father(),
            self.closing()
        ]
        sep = "\n" + "-"*20 + "\n"
        return sep.join(flatten(sequence)) + sep
