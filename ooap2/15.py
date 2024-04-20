from random import random, choice
from math import ceil
from abc import ABC, abstractmethod


class Hero(ABC):

    BASIC_MOVEMENT = 1000

    def __init__(self, attack, defence, knowledge, power):
        # эксплуатация "геройской" тематики в учебных целях
        # private поля класса
        self.__attack = attack
        self.__defence = defence
        self.__knowledge = knowledge
        self.__power = power

        self.__movement = Hero.BASIC_MOVEMENT

        self.artifacts = []

    # private-методы класса
    def __check_movement_artifact(self):
        self.__movement = Hero.BASIC_MOVEMENT
        for artifact in self.artifacts:
            if artifact.has_movement_modifier():
                self.__movement += artifact.movement_modifier

    # protected-методы класса
    @staticmethod
    def _damage_creature(self, my_creature, some_creature):
        summary_attack = my_creature.get_attack()
        summary_defence = some_creature.get_defense()

        coefficient = (summary_attack - summary_defence) * 0.1
        if coefficient < 0.3:
            coefficient = 0.3

        if coefficient > 5:
            coefficient = 5

        damage = ceil(my_creature.get_damage() * coefficient)

        return damage

    @abstractmethod
    def _get_parameter_for_level_up(self):
        pass

    @abstractmethod
    def _get_skill_for_level_up(self):
        pass

    # public_методы класса
    def get_attack(self):
        attack = self.__attack
        for artifact in self.artifacts:
            if artifact.has_attack_modifier():
                attack += artifact.get_attack_modifier()
        return attack

    # Функцию level_up можно спокойно организовать, как вложенная пачка if-else.
    # В классе hero можно сделать атрибут, который принимает значение из enumeration Knight, Priest, Barbarion, Shaman
    # и т.д. И потом запускать if hero_class == Hero.Knight <...> elif и т.д. Проблема в том, что в каждом замке в
    # Героях есть 2 типа героев, а замков изначально 8. Потом, когда базовые классы уже забетонированы, при появлении
    # нового замка придётся добавлять ещё 2 типа героев, а значит придётся править базовый класс Hero, и вносить
    # изменения во все функции, где упоминается проверка класса героя. Наплодить ошибок в такой парадигме легче лёгкого.
    # Лучше, конечно, отказаться от атрибута в пользу наследования.
    def level_up(self):
        parameter = self._get_parameter_for_level_up()
        skill = self._get_skill_for_level_up()
        return parameter, skill


class Knight(Hero):

    def _get_parameter_for_level_up(self):
        number = random()
        if number <= 0.1:
            return 'knowledge'
        elif number <= 0.2:
            return 'power'
        elif number <= 0.6:
            return 'attack'
        else:
            return 'defense'

    def _get_skill_for_level_up(self):
        return choice(['lidership', 'luck', 'attack', 'defense'])

    def check_movement_artifact(self):
        super().__check_movement_artifact()


if __name__ == '__main__':
    christian = Knight(3, 2, 1, 1)
    print(christian.level_up())
