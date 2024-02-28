from typing import Final
from Node import Node


class Queue:

    HEAD_NIL: Final = 0
    HEAD_OK: Final = 1
    TAIL_NIL: Final = 0
    TAIL_OK: Final = 1
    DEQUEUE_NIL: Final = 0
    DEQUEUE_OK: Final = 1
    DEQUEUE_ERR: Final = 2

    def __init__(self):
        self._head = None
        self._tail = None
        self._depth = 0
        self._head_status = self.HEAD_NIL
        self._tail_status = self.TAIL_NIL
        self._dequeue_status = self.DEQUEUE_NIL

    def __len__(self):
        return self._depth

    # команда
    # предусловие: нет
    # постусловие: увеличение очереди на 1 элемент (добавление в хвост очереди)
    def _enqueue(self, value):
        new_node = Node(value)
        if self._head_status == self.HEAD_NIL:
            self._head = new_node
            self._head_status = self.HEAD_OK
        else:
            self._tail.set_next(new_node)
            new_node.set_previous(self._tail)
        self._tail = new_node
        self._tail_status = self.TAIL_OK
        self._depth += 1

    # запрос
    # предусловие: непустая очередь
    # постусловие: возврат значения из головы очереди (уменьшение очереди на 1 элемент)
    def _dequeue(self):
        if self._head_status == self.HEAD_OK:
            value = self._head.get_value()
            if self._depth == 1:
                self.__init__()
            else:
                self._head = self._head.get_next()
                self._head.set_previous(None)
                self._depth -= 1
            self._dequeue_status = self.DEQUEUE_OK
        else:
            value = 0
            self._dequeue_status = self.DEQUEUE_ERR
        return value

    # запросы получения статусов
    def get_head_status(self):  # успешно; пустая очередь
        return self._head_status

    def get_tail_status(self):  # успешно; пустая очередь
        return self._tail_status

    def get_dequeue_status(self):  # успешно: пустая очередь
        return self._dequeue_status
