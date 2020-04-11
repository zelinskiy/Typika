import common

class Ectenia:
    def __init__(self, priest=False, short=False):
        self.common = common.Common()
        self.priest = priest
        self._short = short

    @property
    def short(self):
        return self._short

    @short.setter
    def set_short(self, val):
        self._short = val
        self.common.short = val

    def great(self):
        return self.common.kyrie_eleison_12()

    def supplication(self):
        return self.common.kyrie_eleison_12()

    def small(self):
        return self.common.kyrie_eleison_3()

    def fervent(self):
        return self.common.kyrie_eleison_40()

    def vespers_supplication(self):
        return self.common.kyrie_eleison_12()
