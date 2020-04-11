from typika_module import TypikaModule
import util

class Common(TypikaModule):
    def __init__(self, short, priest):
        super().__init__(short, priest)

    def load(self, fname):
        path = "texts/slav/common/"
        if self.short:
            path += "short/"
        return util.load(path + fname + ".txt")

    def through_the_prayers_of_our_holy_fathers(self):
        return self.load("through_the_prayers_of_our_holy_fathers")

    def glory_to_thee_our_God(self):
        return self.load("glory_to_thee_our_God")

    def heavenly_king(self):
        return self.load("heavenly_king")

    def our_father(self):
        return self.load("our_father")

    def glory_and_now(self):
        return self.load("glory_and_now")

    def trisagion(self):
        return self.load("trisagion")

    def come_let_us_worship(self):
        return self.load("come_let_us_worship")

    def most_holy_trinity(self):
        return self.load("most_holy_trinity")

    def hail_Mary(self):
        return self.load("hail_Mary")

    def more_honourable_cherubim(self):
        return self.load("more_honourable_cherubim")

    def kyrie_eleison_40(self):
        return self.load("kyrie_eleison_40")

    def kyrie_eleison_12(self):
        return self.load("kyrie_eleison_12")

    def kyrie_eleison_3(self):
        return self.load("kyrie_eleison_3")

    def ephrem_prayer(self):
        return self.load("ephrem_prayer")

    def let_lords_name_be_blessed(self):
        return self.load("let_lords_name_be_blessed")

    def axios_estin(self):
        return self.load("axios_estin")

    def alleluia(self):
        return self.load("alleluia")
