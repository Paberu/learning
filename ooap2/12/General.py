from typing import final, TypeVar
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


class Void(General, Any):

    pass


if __name__ == '__main__':
    obj = General()
    print(obj)
    print(obj.__dict__)
    obj.print()
    obj.serialize()
