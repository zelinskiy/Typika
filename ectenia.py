import common
from typika_module import TypikaModule

class Ectenia(TypikaModule):
    def __init__(self, short, priest):
        super().__init__(short, priest)
        self.common = common.Common(short, priest)

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
