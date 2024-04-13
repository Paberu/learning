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
    # christian.__attack += 1
    # у объекта Knight нет аттрибута __attack, он не может обратиться к private-полю родительского объекта

    print(christian.get_attack())
    # 1. Публичный метод родителя публичен и у потомка

    # 2. Публичный метод родителя не удастся сделать скрытым у потомка, т.к. сокрытие методов происходит добавлением
    # префикса _ к имени функции, а get_attack, _get_attack и __get_attack - это разные функции.

    # 3. Скрытый метод родителя публичен у потомка. Похожая ситуация с п.2. Это не вполне раскрытие, это создание
    # похожего метода и т.п. Хотя как по мне, это вполне себе похоже на антипаттерн Паблик Морозов.
    christian.check_movement_artifact()
    # В реализации
    # def check_movement_artifact(self):
    #     self.__check_movement_artifact()
    # и в реализации
    # def check_movement_artifact(self):
    #     super().__check_movement_artifact()
    # вообще не работает, т.к. метода _Knight__check_movement_artifact нет ни в классе Knight, ни в классе Hero.

    # 4. Из сказанного выше следует и следующий вывод: private-методы родителя не становятся private-методами
    # потомков. Т.к. эти методы существуют в общем пространстве имён и полное имя метода будет таковым:
    # _Knight__check_movement_artifact() или _Hero__check_movement_artifact
