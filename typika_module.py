from util import traverse_props

class TypikaModule:
    def __init__(self, short=False, priest=False):
        self._short = short
        self.priest = priest

    @property
    def short(self):
        return self._short

    def _set_short(self, value):
        self._short = value

    def set_short(self, value):
        traverse_props(self, lambda x, s: x._set_short(value), TypikaModule, "short", [])
