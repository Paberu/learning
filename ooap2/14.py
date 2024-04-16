from typing import final, TypeVar, Union
import copy
import pickle

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
    @staticmethod
    def assignment_attempt(target, source):
        if issubclass(source.__class__, target.__class__):
            target = source
        else:
            target = Void()
        return target

    # requests:
    @final
    def __eq__(self, other: _T) -> bool:
        return self.__dict__ == other.__dict__

    @final
    def __repr__(self) -> str:
        s = f'<"{self.__class__.__name__}" instance (id={id(self)})>'
        return s

    @final
    def clone(self) -> _T:
        clone = copy.deepcopy(self)
        return clone

    @final
    def serialize(self) -> bytes:
        bs = pickle.dumps(self)
        return bs

    @final
    @classmethod
    def deserialize(cls, bs: bytes) -> _T:
        instance = pickle.loads(bs)
        return instance

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

    # method statuses requests:
    @final
    def get_copy_status(self) -> int:
        """Return status of last copy_to() call:
        one of the COPY_* constants."""
        return self._copy_status


class Any(General):

    pass


class SomeAddibleType(Any):

    def __init__(self, value: Union[int, float, str]):
        super().__init__()
        if not isinstance(value, Union[int, float, str]):
            Void.__init__()
        else:
            self.value = value

    def __add__(self, other):
        if isinstance(other.value, str) or isinstance(self.value, str):
            return SomeAddibleType(str(self.value) + str(other.value))

        if isinstance(other.value, float) or isinstance(self.value, float):
            return SomeAddibleType(float(self.value) + float(other.value))

        return SomeAddibleType(self.value + other.value)

    def __repr__(self):
        return f'SomeAddibleType, inner_value={self.value}, with type {type(self.value)}'


class Vector(Any):

    def __init__(self, value=None):
        super().__init__()
        self.inner_self = []
        if value is not None:
            self.inner_self.append(value)

    def __len__(self):
        return len(self.inner_self)

    def __add__(self, other):
        if len(self) != len(other):
            return Void()

        result = Vector()
        result.inner_self = [None] * len(self)
        for i in range(len(self)):
            result.inner_self[i] = self.inner_self[i] + other.inner_self[i]

        return result

    def add(self, value):
        self.inner_self.append(value)


class Void(SomeAddibleType):

    def __init__(self):
        pass

    def __add__(self, other):
        return Void()


if __name__ == '__main__':
    vector1 = Vector()
    vector2 = Vector()

    vector1.add(SomeAddibleType(4))
    vector2.add(SomeAddibleType(7))

    vector1.add(SomeAddibleType(8))
    vector2.add(SomeAddibleType(1.2))

    vector1.add(SomeAddibleType('n'))
    vector2.add(SomeAddibleType(4))

    result_vector = vector1 + vector2
    print(result_vector)

    vector3 = Vector()
    vector3.add(SomeAddibleType(5))
    vector3.add(SomeAddibleType('mnm'))
    print(vector3 + vector2)
