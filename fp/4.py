from pymonad.tools import curry
from pymonad.maybe import Just, Nothing, Maybe
from pymonad.list import List, ListMonad


@curry(2)
def add(x, y):
    return x + y


add10 = add(10)
print(Just(9).then(add10))
print(ListMonad(1, 2, 3, 4).then(add10))
