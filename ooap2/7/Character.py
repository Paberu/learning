from abc import ABC, abstractmethod
from WeaponBehaviour import WeaponBehaviour


class Character(ABC):

    def __init__(self, weapon_behaviour: WeaponBehaviour):
        self.weapon_behaviour = weapon_behaviour

    # абстрактный метод даёт возможность вызывать метод fight у объекта не задумываясь, каким из потомков Character
    # является этот объект
    @abstractmethod
    def fight(self):
        pass

    def set_weapon_behaviour(self, weapon_behaviour):
        self.weapon_behaviour = weapon_behaviour


class Knight(Character):
    # совершенно не важно, кем наносится урон. Есть возможность вызвать метод fight у объекта, а как этот метод
    # будет реализован, не интересует ни пользователя, ни интерпретатор. В Java/C# это было бы ещё более наглядно:
    # Character player1 = new Knight()
    # Character player2 = new Troll()
    # Я всё больше склоняюсь к мнению, что динамическая типизация a-la Python, это в какой-то степени неудобно.
    # А нестрогая динамическая типизация a-la JavaScript - это и вовсе кощунственно.
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
