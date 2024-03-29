from typing import Final


class BoundedStack:

    # интерфейс класса, реализующий АТД Stack
    POP_NIL: Final = 0
    POP_OK: Final = 1
    POP_ERR: Final = 2
    PEEK_NIL: Final = 0
    PEEK_OK: Final = 1
    PEEK_ERR: Final = 2
    PUSH_NIL: Final = 0
    PUSH_OK: Final = 1
    PUSH_ERR: Final = 2

    def __init__(self, size=32):  # конструктор
        self.__stack = []  # пустой список/стек
        self.__size = size

        # начальные статусы для предусловий peek(), pop() и push()
        self.__peek_status = BoundedStack.PEEK_NIL
        self.__pop_status = BoundedStack.POP_NIL
        self.__push_status = BoundedStack.PUSH_NIL

    # Python требует, чтобы все поля объявлялись и инициализировались в конструкторе.
    # Поэтому clear() просто переинициализирует объект
    def clear(self):
        self.__init__(self.size())

    def size(self):
        return len(self.__stack)

    # запросы статусов
    def get_pop_status(self):
        return self.__pop_status

    def get_peek_status(self):
        return self.__peek_status

    def get_push_status(self):
        return self.__push_status

    # предусловие: стек заполнен не полностью
    # постусловие: в стек добавлен новый элемент
    def push(self, value):
        if self.size() < self.__size:
            self.__stack.append(value)
            self.__push_status = BoundedStack.PUSH_OK
        else:
            self.__push_status = BoundedStack.PUSH_ERR

    # предусловие: стек не пустой
    # постусловие: из стека удален верхний элемент
    def pop(self):
        if self.size() > 0:
            self.__stack.pop(-1)
            self.__pop_status = BoundedStack.POP_OK
        else:
            self.__pop_status = BoundedStack.POP_ERR

    # предусловие: стек не пустой
    def peek(self):
        if self.size() > 0:
            result = self.__stack[-1]
            self.__peek_status = BoundedStack.PEEK_OK
        else:
            result = 0
            self.__peek_status = BoundedStack.PEEK_ERR
        return result