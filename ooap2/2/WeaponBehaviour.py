from abc import ABC, abstractmethod
import enum


class DamageType(enum.Enum):
    bludgeoning = 1
    slashing = 2
    piercing = 3


class WeaponBehaviour(ABC):
    # в этом классе описывается интерфейс поведения оружия в игре и задаётся наносимый им урон

    def __init__(self, damage_level):
        self.damage_level = damage_level

    @abstractmethod
    def inflict_damage(self):
        pass

    @abstractmethod
    def get_damage_type(self):
        pass

    def set_damage_level(self, damage_level):
        self.damage_level = damage_level


class KnifeStabBehaviour(WeaponBehaviour):
    # а в этом и последующих классах данные интерфейсы реализуются через наследование.
    # наносимый урон указывать не надо, он задаётся в конструкторе при создании объекта.
    # а вот характер наносимых повреждений зависит от того, как использовать то или иное оружие.

    def inflict_damage(self):
        return self.damage_level / 2

    def get_damage_type(self):
        return DamageType.piercing


class KnifeSlashBehaviour(WeaponBehaviour):

    def inflict_damage(self):
        return self.damage_level / 2

    def get_damage_type(self):
        return DamageType.slashing


class SpearStabBehaviour(WeaponBehaviour):

    def inflict_damage(self):
        return self.damage_level * 2

    def get_damage_type(self):
        return DamageType.piercing


class SpearSlashBehaviour(WeaponBehaviour):

    def inflict_damage(self):
        return self.damage_level * 2

    def get_damage_type(self):
        return DamageType.slashing


class ClubBludgeoningBehaviour(WeaponBehaviour):

    def inflict_damage(self):
        return self.damage_level

    def get_damage_type(self):
        return DamageType.bludgeoning


class MaceBludgeoningBehaviour(WeaponBehaviour):

    def inflict_damage(self):
        return self.damage_level * 2

    def get_damage_type(self):
        return DamageType.bludgeoning
