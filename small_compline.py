from typika_module import TypikaModule
from typika_sign import TypikaSign
from common import Common
from psalter import Psalter
from weekday import Day
from util import flatten

class SmallComplineBuilder(TypikaModule):
    def __init__(self, short, priest):
        super().__init__(short, priest)
        self.typika_sign = TypikaSign.Ferial
        self.day = Day.Mon
        self.common = Common(short, priest)
        self.psalter = Psalter(short, priest)

    def opening(self):
        sequence = [
            self.common.through_the_prayers_of_our_holy_fathers(),
            self.common.glory_to_thee_our_God(),
            self.common.heavenly_king(),
            self.common.trisagion(),
            self.common.glory_and_now(),
            self.common.most_holy_trinity(),
            self.common.kyrie_eleison_3(),
            self.common.glory_and_now(),
            self.common.our_father(),
            self.common.kyrie_eleison_12(),
            self.common.glory_and_now(),
            self.common.come_let_us_worship()
        ]
        return "\n".join(sequence)

    def glory_on_high(self):
        return "Слава во вышних"

    def glory_verses(self):
        return "На всяку нощь"

    def kanon(self):
        return "CURRENT KANON"

    # Зри гл.52 Типикона
    def troparion(self):
        sequence = []
        if self.typika_sign > TypikaSign.Doxology:
            sequence = ["CURRENT KONTAKION"]
        elif self.day == Day.Fri:
            sequence = [
                "CURRENT TROPARION",
                "Апостоли, мученицы",
                "Слава",
                "Со святыми упокой",
                "И ныне",
                "Яко начатки естества",
            ]
        elif self.day == Day.Sat:
            sequence = [
                "TEMPLE TROPARION",
                "CURRENT TROPARION",                
                "Боже отец наших",
                "Иже во всем мире",
                "Слава",
                "Со святыми упокой",
                "И ныне",
                "Молитвами, Господи",
            ]
        return "\n".join(sequence)

    def spotless_undefiled_incorrupt(self):
        return "Нескверная неблазная нетленная"

    def pandect_prayer(self):
        return "И даждь нам владыко"

    def joannicius_prayer(self):
        return "Упование мое"

    def build(self):
        sequence = [
            self.opening(),
            self.psalter.psalm(50),
            self.psalter.psalm(69),
            self.psalter.psalm(142),
            self.glory_on_high(),
            self.glory_verses(),
            self.common.credo(),
            self.kanon(),
            self.common.axios_estin(),
            self.common.trisagion(),
            self.common.most_holy_trinity(),
            self.common.our_father(),
            self.troparion(),
            self.common.kyrie_eleison_40(),
            self.common.for_all_time(),
            self.common.kyrie_eleison_3(),
            self.common.glory_and_now(),
            self.common.more_honourable_cherubim(),
            # bless father
            self.common.through_the_prayers_of_our_holy_fathers(),
            self.spotless_undefiled_incorrupt(),
            self.pandect_prayer(),
            self.joannicius_prayer(),
            self.common.glory_and_now(),
            self.common.kyrie_eleison_3(),
            # bless father
            self.common.through_the_prayers_of_our_holy_fathers(),
        ]
        sep = "\n" + "-"*20 + "\n"
        return sep.join(flatten(sequence)) + sep
