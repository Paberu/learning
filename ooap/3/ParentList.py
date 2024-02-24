from typing import Final


class Node:

    def __init__(self, v):
        self._value = v
        self._next = None
        self._previous = None

    def has_next(self):
        return self._next is not None

    def has_previous(self):
        return self._previous is not None

    def get_next(self):
        return self._next

    def get_previous(self):
        return self._previous

    def set_next(self, node):
        self._next = node
        node._previous = self

    def set_previous(self, node):
        self._previous = node
        node._next = self

    def get_vale(self):
        return self._value


class ParentList:
    HEAD_NIL: Final = 0
    HEAD_OK: Final = 1
    TAIL_NIL: Final = 0
    TAIL_OK: Final = 1
    RIGHT_NIL: Final = 0
    RIGHT_OK: Final = 1
    PUT_RIGHT_NIL: Final = 0
    PUT_RIGHT_OK: Final = 1
    PUT_LEFT_NIL: Final = 0
    PUT_LEFT_OK: Final = 1
    REMOVE_NIL: Final = 0
    REMOVE_OK: Final = 1
    REPLACE_NIL: Final = 0
    REPLACE_OK: Final = 1
    FIND_NIL: Final = 0
    FIND_OK: Final = 1
    FIND_ERR: Final = 2
    GET_NIL: Final = 0
    GET_OK: Final = 1

    # конструктор
    # постусловие: создан новый пустой список
    def __init__(self):
        self._head = None
        self._tail = None
        self._cursor = None

        self._head_status = self.HEAD_NIL
        self._tail_status = self.TAIL_NIL
        self._right_status = self.RIGHT_NIL
        self._put_right_status = self.PUT_RIGHT_NIL
        self._put_left_status = self.PUT_LEFT_NIL
        self._remove_status = self.REMOVE_NIL
        self._replace_status = self.REPLACE_NIL
        self._find_status = self.FIND_NIL
        self._get_status = self.GET_NIL

    # команды
    # предусловие: список не пуст;
    # постусловие: курсор установлен на первый узел в списке
    def head(self):
        if self.get_head_status() == self.HEAD_OK:
            current = self._cursor = self._head
            if current.has_next():
                self._right_status = self.RIGHT_OK
            else:
                self._right_status = self.RIGHT_NIL

    # предусловие: список не пуст;
    # постусловие: курсор установлен на последний узел в списке
    def tail(self):
        if self.get_tail_status() == self.TAIL_OK:
            self._cursor = self._tail
            self._right_status = self.RIGHT_NIL

    # предусловие: правее курсора есть элемент;
    # постусловие: курсор сдвинут на один узел вправо
    def right(self):
        if self.get_right_status() == self.RIGHT_OK:
            current = self._cursor = self._cursor.get_next()
            if not current.has_next():
                self._right_status = self.RIGHT_NIL

    # предусловие: список не пуст;
    # постусловие: следом за текущим узлом добавлен новый узел с заданным значением
    def put_right(self, value):
        if self.get_head_status() == self.HEAD_OK:
            new_node = Node(value)
            current_node = self._cursor
            next_node = current_node.get_next()

            new_node.set_next(next_node)
            new_node.set_previous(current_node)

            current_node.set_next(new_node)
            if self._tail != current_node:
                next_node.set_previous(new_node)
            else:
                self._tail = new_node
                self._right_status = self.RIGHT_NIL
            self._put_right_status = self.PUT_RIGHT_OK

    # предусловие: список не пуст;
    # постусловие: перед текущим узлом добавлен новый узел с заданным значением
    def put_left(self, value):
        if self.get_head_status() == self.HEAD_OK:
            new_node = Node(value)
            current_node = self._cursor
            previous_node = current_node.get_previous()

            new_node.set_previous(previous_node)
            new_node.set_next(current_node)

            current_node.set_previous(new_node)
            if self._head != current_node:
                previous_node.set_next(new_node)
            else:
                self._head = new_node
            self._put_left_status = self.PUT_LEFT_OK

    # предусловие: список не пуст;
    # постусловие: текущий узел удалён, курсор смещён к правому соседу, если он есть, в противном случае
    # курсор смещён к левому соседу, если он есть
    def remove(self):
        if self.get_head_status() == self.HEAD_OK:
            current_node = self._cursor
            if not current_node.has_next() and not current_node.has_previous():  # нет следующего и предыдущего,
                self._head = self._tail = self._cursor = None  # т.е. последний в списке
                self._head_status = self.HEAD_NIL
                self._tail_status = self.TAIL_NIL
                self._right_status = self.RIGHT_NIL
            elif not current_node.next:  # нет следующего, т.е. tail
                current_node.get_previous().set_next(None)
                self._cursor = self._tail = current_node.get_previous()
            elif not current_node.previous:  # нет предыдущего, т.е. head
                current_node.get_next().set_previous(None)
                self._cursor = self._head = current_node.get_next()
            else:  # обычный узел где-то в середине
                current_node.get_previous().set_next(current_node.get_next())
                current_node.get_next().set_previous(current_node.get_previous())
                self._cursor = current_node.get_next()

    # постусловие: список очищен от всех элементов
    def clear(self):
        self._init_()

    # постусловие: новый узел добавлен в хвост списка
    def add_tail(self, value):
        new_node = Node(value)
        if self.get_tail_status() == self.TAIL_OK:
            tail = self._tail
            tail.set_next(new_node)
            new_node.set_previous(tail)
            self._tail = new_node
        else:
            self._head = self._tail = self._cursor = new_node
            self._head_status = self.HEAD_OK
            self._tail_status = self.TAIL_OK
        self._right_status = self.RIGHT_NIL

    # постусловие: в списке удалены все узлы с заданным значением
    def remove_all(self, value):
        self._remove_status = self.REMOVE_NIL
        self._cursor = self._head
        while self._cursor:
            if self._cursor.get_value() == value:
                self.remove()
                self._remove_status = self.REMOVE_OK

    # предусловие: список не пуст;
    # постусловие: значение текущего узла заменено на новое
    def replace(self, value):
        self._replace_status = self.REPLACE_NIL
        if self._cursor:
            self._cursor.set_value(value)
            self._replace_status = self.REPLACE_OK

    # постусловие: курсор установлен на следующий узел с искомым значением, если такой узел найден
    def find(self, value):
        current_node = self._cursor
        self.right()
        found = False
        while self._cursor:
            if self._cursor.get_value() == value:
                found = True
                break
            else:
                self.right()
        if not found:
            self._cursor = current_node

    # запросы
    def get(self):  # предусловие: список не пуст
        if self._cursor:
            return self._cursor.get_value()

    def is_head(self):
        return self.get_head_status() == self.HEAD_OK and self._cursor == self._head

    def is_tail(self):
        return self.get_tail_status() == self.TAIL_OK and self._cursor == self._tail

    def is_value(self):
        return self._cursor and self._cursor.get_value()

    def size(self):
        size = 0
        if self.get_head_status() == self.HEAD_OK:
            current_node = self._head
            while current_node.has_next():
                size += 1
                current_node.next()

    # запросы статусов (возможные значения статусов)
    def get_head_status(self):  # успешно; список пуст
        return self._head_status

    def get_tail_status(self):  # успешно; список пуст
        return self._tail_status

    def get_right_status(self):  # успешно; правее нету элемента
        return self._right_status

    def get_put_right_status(self):  # успешно; список пуст
        return self._put_right_status

    def get_put_left_status(self):  # успешно; список пуст
        return self._put_left_status

    def get_remove_status(self):  # успешно; список пуст
        return self._remove_status

    def get_replace_status(self):  # успешно; список пуст
        return self._replace_status

    def get_find_status(self):  # следующий найден; следующий не найден; список пуст
        return self._find_status

    def get_get_status(self):  # успешно; список пуст
        return self._get_status
