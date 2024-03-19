from abc import ABC, abstractmethod
from WeaponBehaviour import WeaponBehaviour


class Character(ABC):
    # пример взят из книги про паттерны, Паттерн Стратегия прекрасно описывает разделение поведения объекта и самого
    # объекта, даёт возможность потренироваться в наследовании, композиции и полиморфизме

    def __init__(self, weapon_behaviour: WeaponBehaviour):
        # здесь наблюдается композиция, т.к. персонажу присваивается некоторый способ обращения с оружием
        self.weapon_behaviour = weapon_behaviour

    @abstractmethod
    def fight(self):
        pass

    def set_weapon_behaviour(self, weapon_behaviour):
        self.weapon_behaviour = weapon_behaviour


class Knight(Character):
    # необходимость реализации абстрактного метода (а в Python абстрактный метод может и не быть пустым, в нём может
    # содержаться некая базовая функциональность, но при этом метод всё ещё остаётся абстрактным; у меня вопросы к
    # создателям языка), своя для каждого класса - это полиморфизм, т.к. вызов одного и того же метода у объектов
    # разных классов приводит к разным результатам для одного и того же способа обращения с одним и тем же оружием
    def fight(self):
        return {'damage_type': self.weapon_behaviour.get_damage_type(),
                'damage': self.weapon_behaviour.inflict_damage() * 4}


class King(Character):
    # и в то же время класс каждого персонажа наследуется от базового класса Character
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
