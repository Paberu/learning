from collections.abc import Callable
from Any import Any
from Void import Void
from abc import ABC, abstractmethod
from WeaponBehaviour import WeaponBehaviour, SpearStabBehaviour, ClubBludgeoningBehaviour, KnifeStabBehaviour, MaceBludgeoningBehaviour


class Character(Any, ABC):

    def __init__(self, weapon_behaviour: WeaponBehaviour):
        super().__init__()
        self.weapon_behaviour = weapon_behaviour

    # Методу fight не обязательно быть абстрактным в классическом понимании, он может содержать в себе некий базовый
    # функционал и в то же время продолжать называться абстрактным.
    # В данном коде присутствует ковариантность: рассмотрим пример в функции __main__()
    @abstractmethod
    def fight(self):
        return {'damage_type': self.weapon_behaviour.get_damage_type(),
                'damage': self.weapon_behaviour.inflict_damage()}

    def set_weapon_behaviour(self, weapon_behaviour):
        self.weapon_behaviour = weapon_behaviour

    def flee(self):
        print('Hero is running away')
        return Void()


class Knight(Character):

    def fight(self):
        return {'damage_type': self.weapon_behaviour.get_damage_type(),
                'damage': self.weapon_behaviour.inflict_damage() * 4}


class King(Character):

    def fight(self):
        return {'damage_type': self.weapon_behaviour.get_damage_type(),
                'damage': self.weapon_behaviour.inflict_damage() * 1.5}


class Princess(Character):

    def fight(self):
        return {'damage_type': self.weapon_behaviour.get_damage_type(),
                'damage': self.weapon_behaviour.inflict_damage() * 0.75}


class Troll(Character):

    def fight(self):
        return {'damage_type': self.weapon_behaviour.get_damage_type(),
                'damage': self.weapon_behaviour.inflict_damage() * 8}


class GiantTroll(Troll):

    def frighten(self):
        print('Everyone is frightened!')
        return Void()


if __name__ == '__main__':
    knight = Knight(SpearStabBehaviour(4))
    king = King(MaceBludgeoningBehaviour(6))
    princess = Princess(KnifeStabBehaviour(2))
    troll = Troll(ClubBludgeoningBehaviour(8))
    characters = [knight, king, princess, troll]
    for character in characters:
        print(character.fight())

