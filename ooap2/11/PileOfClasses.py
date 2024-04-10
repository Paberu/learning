from collections.abc import Iterable
from abc import ABC, abstractmethod
from typing import final
import copy
import json
import enum


# Хотел уточнить следующее: у меня есть классы, не имеющие потомков: King, Knight, Princess, GiantTroll.
# Они наследуются от Character, который наследуется от Any, который наследуется от General.

# Я создаю класс Void вместо порицаемого None (который null в Python), и делаю его наследником всех четырёх
# классов-листьев.
#
# Далее, поскольку любая функция без return в Python автоматически получает строку return None в качестве завершающей,
# все функции без return (в иерархии от General до последнего King), получают return Void(). Ради этого приходится
# импортировать Void во все файлы, где описаны классы.
#
# Получается ошибка "cannot import name <...> most likely due to a circular import". Импорт по кругу, и привет.
# Я собрал все классы в файл PileOfClasses.py, и, о чудо, всё заработало. Но, очевидно, это не то, что задумывалось.
# Буду думать, как это разрулить.

class General:
    # не нужно наследовать от Object, любой объявленный класс при отсутствии предка автоматически наследует от Object
    def __init__(self):
        pass

    @final
    def copy(self):
        return copy.copy(self)

    @final
    def clone(self):
        return copy.deepcopy(self)

    @final
    def compare(self, another):
        for attr in self.__dict__.keys():
            if another.__getattribute__(attr) != self.__getattribute__(attr):
                return False
        return True

    @final
    def deep_compare(self, another):
        for attr in self.__dict__.keys():
            compare_attr_result = self.__compare(self.__getattribute__(attr), another.__getattribute__(attr))
            if not compare_attr_result:
                return False
        return True

    @staticmethod
    def __compare(one, another):
        one_iterable = isinstance(one, Iterable)
        another_iterable = isinstance(another, Iterable)

        if (one_iterable and not another_iterable) or (not one_iterable and another_iterable):
            return False  # т.к. один - итерируемый, а второй - нет

        if not one_iterable and not another_iterable:  # оба неитерируемы
            return one == another

        # остался случай, когда оба итерируемы
        if len(one) != len(another):
            return False

        for i in range(len(one)):
            if not General.__compare(one[i], another[i]):
                return False
        return True

    @final
    def serialize(self):
        to_dict = {}
        for attr in self.__dict__.keys():
            datapiece = self.__getattribute__(attr)
            if isinstance(datapiece, General):
                to_dict[attr] = datapiece.serialize()
            else:
                to_dict[attr] = datapiece
        return json.dumps(to_dict)

    @final
    def deserialize(self, data):
        from_dict = json.loads(data)
        for key in from_dict.keys():
            self.__setattr__(key, from_dict[key])
        return Void()

    def __str__(self):
        result = str(type(self))
        for attr in self.__dict__.keys():
            result += f'{attr}: {self.__getattribute__(attr)}'
        return result

    @final
    def print(self):
        return str(self)

    @final
    def check_type(self, type_to_check):
        return isinstance(self, type_to_check)

    @final
    def get_real_type(self):
        return type(self)


class Any(General):

    pass


class Character(Any, ABC):

    def __init__(self, weapon_behaviour):
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


class Void(GiantTroll, Troll, King, Knight, Princess, KnifeStabBehaviour, KnifeSlashBehaviour, SpearStabBehaviour,
           SpearSlashBehaviour, MaceBludgeoningBehaviour, ClubBludgeoningBehaviour, WeaponBehaviour, Character):
    # если честно, такой подход кажется изрядно излишним; если классов без наследников будет 25, то и в предки Void
    # записать придётся все 25 классов - мне это кажется чрезмерным усложнением

    def __init__(self):
        pass


if __name__ == '__main__':
    knight = Knight(SpearStabBehaviour(4))
    king = King(MaceBludgeoningBehaviour(6))
    princess = Princess(KnifeStabBehaviour(2))
    troll = GiantTroll(ClubBludgeoningBehaviour(8))
    characters = [knight, king, princess, troll]

    data = troll.serialize()
    troll2 = GiantTroll(ClubBludgeoningBehaviour(0))
    deserial = troll2.deserialize(data)
    if isinstance(deserial, Void):
        print('Troll successfully deserialized into Giant Troll. Magic!')

    runaway = princess.flee()
    if isinstance(runaway, Void):
        print('Princess is running away from the Void!')
