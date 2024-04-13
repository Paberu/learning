from collections.abc import Iterable
from typing import final, TypeVar
import copy
import json

_T = TypeVar('_T')


class General(object):

    COPY_NIL = 0       # copy_to() not called yet
    COPY_OK = 1        # last copy_to() call completed successfully
    COPY_ATTR_ERR = 2  # other object have no attribute copied from this object

    def __get_status_fields(self) -> set:
        fields = set(attr for attr in dir(self) if attr.endswith('status'))
        return fields

    def __init__(self, *args, **kwargs):
        self._copy_status = self.COPY_NIL

    # commands:
    @final
    def copy_to(self, other: _T) -> None:
        # Deep-copy of attributes of **self** to **other** with ignoring status-attributes.
        status_fields = self.__get_status_fields()
        copy_attrs = filter(lambda a: a not in status_fields, dir(self))

        if not all((hasattr(other, a) for a in copy_attrs)):
            self._copy_status = self.COPY_ATTR_ERR
        else:
            for attr in copy_attrs:
                value = copy.deepcopy(getattr(self, attr))
                setattr(other, attr, value)
            self._copy_status = self.COPY_OK
    @final
    def clone(self):
        new_object = self.__class__.__new__()
        self.copy_to(new_object)
        if self._copy_status == self.COPY_OK:
            return new_object
        else:
            return Void()

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
            to_dict[attr] = self.__getattribute__(attr)
        return json.dumps(to_dict)

    @final
    def deserialize(self, data):
        from_dict = json.loads(data)
        for key in from_dict.keys():
            self.__setattr__(key, from_dict[key])
        return Void

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


class Void(General, Any):

    pass


if __name__ == '__main__':
    obj = General()
    print(obj)
    print(obj.__dict__)
    obj.print()
    obj.serialize()
