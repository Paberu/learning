from dataclasses import dataclass

@dataclass(frozen=True)
class Element:
    symbol: str
    EMPTY = '0'

    def __init__(self, c: str):
        object.__setattr__(self, 'symbol', c)

    @classmethod
    def empty(cls):
        return Element(cls.EMPTY)


