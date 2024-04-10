from abc import ABC, abstractmethod
from Any import Any
import enum


class DamageType(enum.Enum):
    bludgeoning = 1
    slashing = 2
    piercing = 3


class WeaponBehaviour(Any, ABC):

    def __init__(self, damage_level):
        super().__init__()
        self.damage_level = damage_level

    # здесь всё то же самое - наличие абстрактных методов позволяет выбирать реализацию метода на ходу, в момент
    # выявления к кому из потомков относится данный объект.

    @abstractmethod
    def inflict_damage(self):
        pass

    @abstractmethod
    def get_damage_type(self):
        pass

    def set_damage_level(self, damage_level):
        self.damage_level = damage_level


class KnifeStabBehaviour(WeaponBehaviour):

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
