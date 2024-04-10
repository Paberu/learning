from Character import GiantTroll, Troll, King, Knight, Princess, Character
from WeaponBehaviour import (KnifeSlashBehaviour, KnifeStabBehaviour, SpearStabBehaviour, SpearSlashBehaviour,
                             MaceBludgeoningBehaviour, ClubBludgeoningBehaviour, WeaponBehaviour)


class Void(GiantTroll, Troll, King, Knight, Princess, KnifeStabBehaviour, KnifeSlashBehaviour, SpearStabBehaviour,
           SpearSlashBehaviour, MaceBludgeoningBehaviour, ClubBludgeoningBehaviour, WeaponBehaviour, Character):
    # если честно, такой подход кажется изрядно излишним; если классов без наследников будет 25, то и в предки Void
    # записать придётся все 25 классов - мне это кажется чрезмерным усложнением

    def __init__(self):
        pass


if __name__ == '__main__':
    knight = Knight(SpearStabBehaviour(4))
    king = King(MaceBludgeoningBehaviour(6))
    princess = Princess(KnifeStabBehaviour(2))
    troll = GiantTroll(ClubBludgeoningBehaviour(8))
    characters = [knight, king, princess, troll]

    data = troll.serialize()
    troll2 = GiantTroll()
    deserial = troll2.deserialize(data)
    if isinstance(deserial, Void):
        print('Troll successfully deserialized into Giant Troll. Magic!')

    runaway = princess.flee()
    if isinstance(runaway, Void):
        print('Princess is running away from the Void!')


