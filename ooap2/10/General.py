from collections.abc import Iterable
from typing import final
import copy
import json


class General:
    # не нужно наследовать от Object, любой объявленный класс при отсутствии предка автоматически наследует от Object
    def __init__(self):
        pass

    # оставляю данную функцию в комментариях как иллюстрацию кода, не имеющего смысла:
    # another в теле функции - не тот же самый another, что среди аргументов функции (аргументы нельзя переопределить)
    # self = copy.deepcopy(another) тоже не имее смысла, т.к. просто создаётся локальная переменная self
    # остаётся только каноничный по ФП return, а возвращать неглубокую копию не вижу смысла

    # def copy(self, another):
    #     another = copy.deepcopy(self)

    # на всякий случай, сделаю возврат неглубокого копирования:
    def copy(self):
        return copy.copy(self)

    def clone(self):
        return copy.deepcopy(self)

    def compare(self, another):
        for attr in self.__dir__():
            if another.__getattr__(attr) != self.__getattribute__(attr):
                return False
        return True

    def deep_compare(self, another):
        for attr in self.__dir__():
            compare_attr_result = self.__compare(self.__getattribute__(attr), another.__getattr__(attr))
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
        for attr in self.__dir__():
            to_dict[attr] = self.__getattribute__(attr)
        return json.dumps(to_dict)

    @final
    def deserialize(self, data):
        from_dict = json.loads(data)
        for key in from_dict.keys():
            self.__setattr__(key, from_dict[key])

    def __str__(self):
        result = ''
        for attr in self.__dir__():
            result += f'{attr}: {self.__getattribute__(attr)}'

    def print(self):
        return str(self)

    def check_type(self, type_to_check):
        return isinstance(self, type_to_check)

    def get_real_type(self):
        return type(self)
