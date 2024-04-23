from abc import ABC, abstractmethod


class Unit(ABC):

    def __init__(self, attack, defence, health, movement):
        self._attack = attack
        self._defence = defence
        self._health = health
        self._movement = movement

    @abstractmethod
    def get_magical_damage(self, magical_damage):
        self._health -= magical_damage

    def get_health(self):
        return self._health


class GreenDragon(Unit):

    def __init__(self):
        super().__init__(20, 20, 300, 10)

    def get_magical_damage(self, magical_damage):
        self._health -= magical_damage / 2
        

class RockBird(Unit):
    def __init__(self):
        super().__init__(10, 10, 100, 13)
        
    def get_magical_damage(self, magical_damage):
        super().get_magical_damage(magical_damage)

