from pymonad.tools import curry
from pymonad.maybe import Just, Maybe, Nothing
from pymonad.list import ListMonad


@curry(2)
def to_left(num: int, birds: Maybe):
    left, right = birds
    if abs((left + num) - right) > 4:
        return Nothing
    else:
        return Just([left+num, right])


@curry(2)
def to_right(num: int, birds: Maybe):
    left, right = birds
    if abs((right + num) - left) > 4:
        return Nothing
    else:
        return Just([left, right + num])


@curry(1)
def banana(birds: Maybe):
    return Nothing


def show(birds: Maybe):
    return not birds.is_nothing()


begin = Just([0, 0])

finale = begin.bind(to_left(2)).bind(to_right(5)).bind(to_left(2))
finale2 = begin.bind(to_left(3)).bind(to_right(5)).bind(to_left(-3))
finale3 = begin.bind(to_left(2)).bind(to_right(2)).bind(banana).bind(to_left(2)).bind(to_right(2))
print(show(finale))
print(show(finale2))
print(show(finale3))
