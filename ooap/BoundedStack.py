from typing import Final

class BoundedStack:

    # скрытые поля
    # private List<T> stack; // основное хранилище стека
    # private int peek_status; // статус запроса peek()
    # private int pop_status; // статус команды pop()

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

    def push(self, value):
        if self.size() == self.__size:  # размер внутреннего списка может сравняться с ограничением, но не превысить его
            raise IndexError('Stack is full, pop some items.')
        self.__stack.append(value)

    def pop(self):
        if self.size() > 0:
            self.__stack.pop(-1)
            self.__pop_status = BoundedStack.POP_OK
        else:
            self.__pop_status = BoundedStack.POP_ERR

    def peek(self):
        if self.size() > 0:
            self.__peek_status = BoundedStack.PEEK_OK
            return self.__stack[-1]
        self.__peek_status = PEEK_ERR
        return 0

