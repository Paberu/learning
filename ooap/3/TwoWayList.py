from typing import Final
from ParentList import ParentList, Node


class TwoWayList(ParentList):

    LEFT_NIL: Final = 0
    LEFT_OK: Final = 1

    def __init__(self):
        super().__init__()
        self._left_status = self.LEFT_NIL

    def head(self):
        super().head()
        self._left_status = self.LEFT_NIL

    def tail(self):
        super().tail()
        if self._cursor.has_previous():
            self._left_status = self.LEFT_OK
        else:
            self._left_status = self.LEFT_NIL

    def right(self):
        super().right()
        if self._head != self._cursor:
            self._left_status = self.LEFT_OK

    def left(self):
        if self.get_left_status() == self.LEFT_OK:
            current = self._cursor = self._cursor.get_previous()
            if not current.has_previous():
                self._left_status = self.LEFT_NIL

    def put_right(self, value):
        super().put_right(value)
        if self.get_head_status() == self.HEAD_OK:
            self._left_status = self.LEFT_OK

    def put_left(self, value):
        super().put_left(value)
        if self.get_head_status() == self.HEAD_OK and self._cursor != self._head:
            self._left_status = self.LEFT_OK
        else:
            self._left_status = self.LEFT_NIL

    def remove(self):
        if self._cursor and self._cursor.has_previous():
            self._left_status = self.LEFT_OK
        else:
            self._left_status = self.LEFT_NIL

    def clear(self):
        self.__init__()

    def add_tail(self, value):
        super().add_tail(value)
        if self._head != self._tail:
            self._left_status = self.LEFT_OK

    def get_left_status(self):
        return self._lef_status
