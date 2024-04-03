from collections.abc import Callable
from abc import ABC, abstractmethod
from WeaponBehaviour import WeaponBehaviour, SpearStabBehaviour, ClubBludgeoningBehaviour, KnifeStabBehaviour, MaceBludgeoningBehaviour


class Character(ABC):

    def __init__(self, weapon_behaviour: WeaponBehaviour):
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


# неэлегантно: код вне классов. Пишу такое только ради того, чтобы попробовать контрвариантность, которая чуть не
# сломала мне голову
def use_special_ability(ability: Callable[[Troll], None], troll: Troll) -> None:
    ability(troll)


def task_for_giant_troll(giant_troll):
    giant_troll.frighten()


def task_for_hero(hero):
    hero.flee()


if __name__ == '__main__':
    # ниже пример кода с ковариантностью: нам не важно, кто из наследников Character наносит удар (чья реализация fight
    # вызывается в данный момент), хотя в ЯВУ типа Python это не так очевидно и не так элегантно. Подозреваю, что для
    # изучения ООАП стоило выбрать яык со статической типизацией, хотя бы та же Java.
    knight = Knight(SpearStabBehaviour(4))
    king = King(MaceBludgeoningBehaviour(6))
    princess = Princess(KnifeStabBehaviour(2))
    troll = Troll(ClubBludgeoningBehaviour(8))
    characters = [knight, king, princess, troll]
    for character in characters:
        print(character.fight())

    # пробую разобраться с контрвариантностью:
    giant_troll = GiantTroll(ClubBludgeoningBehaviour(10))
    use_special_ability(task_for_giant_troll, giant_troll)
    use_special_ability(task_for_hero, giant_troll)
    # всё, что может сделать с персонажем, можно сделать и с гигантским троллем, но не наоборот.

    use_special_ability(task_for_giant_troll, troll)
    # вот здесь будет ошибка: такого умения нет у обычного тролля.

# В целом, мне кажется, что я достиг понимания того, зачем нам нужны такие игры с контрвариантностью, но я буду
# придерживаться классического подхода к наследованию
