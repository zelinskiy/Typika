class TypikaModule:
    def __init__(self, short=False, priest=False):
        self._short = short
        self.priest = priest

    @property
    def short(self):
        return self._short

    @short.setter
    def set_short(self, value):
        self._short = val
        for child in vars(self):
            x = getattr(self, child)
            if x is not None and getattr(x, "short") is not None:
                x.short = self._short
