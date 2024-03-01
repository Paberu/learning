from typing import Final
from Node import Node


class ParentQueue:

    HEAD_NIL: Final = 0
    HEAD_OK: Final = 1
    TAIL_NIL: Final = 0
    TAIL_OK: Final = 1
    DEQUEUE_NIL: Final = 0
    DEQUEUE_OK: Final = 1
    DEQUEUE_ERR: Final = 2
    PEEK_NIL: Final = 0
    PEEK_OK: Final = 1
    PEEK_ERR: Final = 2

    def __init__(self):
        self._head = None
        self._tail = None
        self._depth = 0
        self._head_status = self.HEAD_NIL
        self._tail_status = self.TAIL_NIL
        self._dequeue_status = self.DEQUEUE_NIL
        self._peek_status = self.PEEK_NIL

    def __len__(self):
        return self._depth

    def size(self):
        return self._depth

    def __str__(self):
        return str(self._peek_head()) + ' ' + str(self._peek_tail())

    # команды
    # предусловие: нет
    # постусловие: увеличение очереди на 1 элемент (добавление в хвост очереди)
    def _add_tail(self, value):
        new_node = Node(value)
        if self.get_head_status() == self.HEAD_NIL:
            self._head = new_node
            self._head_status = self.HEAD_OK
        else:
            self._tail.set_next(new_node)
            new_node.set_previous(self._tail)
        self._tail = new_node
        self._tail_status = self.TAIL_OK
        self._depth += 1

    # предусловие: нет
    # постусловие: увеличение очереди на 1 элемент (добавление в хвост очереди)
    def _add_head(self, value):
        new_node = Node(value)
        if self.get_tail_status() == self.TAIL_NIL:
            self._tail = new_node
            self._tail_status = self.TAIL_OK
        else:
            self._head.set_previous(new_node)
            new_node.set_next(self._head)
        self._head = new_node
        self._head_status = self.HEAD_OK
        self._depth += 1

    # запросы
    # предусловие: непустая очередь
    # постусловие: возврат значения из головы очереди (уменьшение очереди на 1 элемент)
    def _pop_head(self):
        value = 0
        if self.get_head_status() == self.HEAD_OK:
            value = self._head.get_value()
            if self.size() == 1:
                self.__init__()
            else:
                self._head = self._head.get_next()
                self._head.set_previous(None)
                self._depth -= 1
            self._dequeue_status = self.DEQUEUE_OK
        else:
            self._dequeue_status = self.DEQUEUE_ERR
        return value

    # предусловие: непустая очередь
    # постусловие: возврат значения из головы очереди (уменьшение очереди на 1 элемент)
    def _pop_tail(self):
        value = 0
        if self.get_tail_status() == self.TAIL_OK:
            value = self._tail.get_value()
            if self.size() == 1:
                self.__init__()
            else:
                self._tail = self._tail.get_previous()
                self._tail.set_next(None)
                self._depth -= 1
            self._dequeue_status = self.DEQUEUE_OK
        else:
            self._dequeue_status = self.DEQUEUE_ERR
        return value

    # предусловие: непустая очередь
    # постуслосие: возврат значения из головы очереди
    def _peek_head(self):
        if self.get_head_status() == self.HEAD_OK:
            value = self._head.get_value()
            self._peek_status = self.PEEK_OK
        else:
            value = 0
            self._peek_status = self.PEEK_ERR
        return value

    # предусловие: непустая очередь
    # постуслосие: возврат значения из хвоста очереди
    def _peek_tail(self):
        if self.get_tail_status() == self.TAIL_OK:
            value = self._tail.get_value()
            self._peek_status = self.PEEK_OK
        else:
            value = 0
            self._peek_status = self.PEEK_ERR
        return value

    # запросы получения статусов
    def get_head_status(self):  # успешно; пустая очередь
        return self._head_status

    def get_tail_status(self):  # успешно; пустая очередь
        return self._tail_status

    def get_dequeue_status(self):  # успешно; пустая очередь
        return self._dequeue_status

    def get_peek_status(self):  # успешно; пустая очередь
        return self._peek_status
