from abc import ABC, abstractmethod
from WeaponBehaviour import WeaponBehaviour


class Character(ABC):
    # возьму пример из предыдущего задания

    def __init__(self, weapon_behaviour: WeaponBehaviour, armor: float):
        self.weapon_behaviour = weapon_behaviour
        self.armor = armor

    @abstractmethod
    def fight(self):
        pass

    def set_weapon_behaviour(self, weapon_behaviour):
        self.weapon_behaviour = weapon_behaviour

    def set_armored(self, armor):
        self.armor = armor


class Knight(Character):

    # здесь показана специализация класса-родителя наследником
    def __init__(self, weapon_benaviour):
        super().__init__(weapon_benaviour, 0.3)

    def fight(self):
        return {'damage_type': self.weapon_behaviour.get_damage_type(),
                'damage': self.weapon_behaviour.inflict_damage() * 4}


class NPC(Character):

    # здесь класс-родитель расширяется дополнительными опциями, персонажу можно передать ссылку на скрипт управления,
    # тогда все перемещения, способ ведения боя, наносимый урон передаются в реализованные функции
    # в случае наличия для behaviour_style значения 'user_driven' класс NPC вырождается в Knight, например
    def __init__(self, weapon_behaviour, armor, behaviour_style):
        super().__init__(weapon_behaviour, armor)
        self.behaviour_style = behaviour_style

    def fight(self):
        return {'damage_type': self.weapon_behaviour.get_damage_type(),
                'damage': self.weapon_behaviour.inflict_damage() * self.behaviour_style.fight_coeff}