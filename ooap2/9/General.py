from collections.abc import Iterable

class General: # не нужно наследовать от Object, любой объявленный класс при отсутствии предка автоматически наследует от Object

    def __init__(self):
        pass
    def __copy(self, another) -> None:
        for attr in self.__dir__():
            another.__setattr__(attr, self.__getattribute__(attr))

    def __clone(self):
        new_object = General()
        return self.__copy(new_object)
    def __compare(self, another):
        for attr in self.__dir__():
            if another.__getattr__(attr) != self.__getattribute__(attr):
                return False
        return True

    def __deep_compare(self, another):
        for attr in set.__dir__():
            attr_for_check = self.__getattribute__(attr)
            if isinstance(attr_for_check, Iterable):
                if
            elif another.__getattr__(attr) != self.__getattribute__(attr):
                return False

    @staticmethod
    def __compare_iterables(one, another):
        if not isinstance(one, Iterable) or not isinstance(another, Iterable):
            return False
        if len(one) != len(another):
            return False

        for i in range(len(one)):
            if one[i] != another[i]:
                return False


    def __serialize(self):
        pass

    def __deserialize(self):
        pass

    def __str__(self):
        pass

    def __
