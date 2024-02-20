from typing import Final


class LinkedList:

    LIST_EMPTY: Final = 0
    LIST_NOT_EMPTY: Final = 1
    FIND_NIL: Final = 0
    FIND_OK: Final= 1
    FIND_ERR: Final = 2

    def __init__(self):
        self.__list = []
        self.__cursor = 0  # указывает на индекс текущего элемента в списке

        self.__list_status = LinkedList.LIST_EMPTY
        self.__find_status = LinkedList.FIND_NIL

    # запросы:
    def size(self):
        return len(self.__list)

    # предусловие: список должен быть непустой
    def get(self):
        if self.__list_status == LinkedList.LIST_NOT_EMPTY:
            return self.__list[self.__cursor]

    # предусловие: список должен быть непустой
    def is_head(self):
        if self.__list_status == LinkedList.LIST_NOT_EMPTY:
            return self.__cursor == 0

    # предусловие: список должен быть непустой
    def is_tail(self):
        if self.__list_status == LinkedList.LIST_NOT_EMPTY:
            return self.__cursor == self.size() - 1

    # предусловие: список должен быть непустой
    def is_value(self):
        if self.__list_status == LinkedList.LIST_NOT_EMPTY:
            return True

    # предусловие: список должен быть непустой
    def find(self, value):
        if self.__list_status == LinkedList.LIST_NOT_EMPTY:
            try:
                result = self.__list.index(value, self.__cursor)
                self.__find_status = LinkedList.FIND_OK
            except ValueError:
                result = 0
                self.__find_status = LinkedList.FIND_ERR
            return result

    # команды:

    # предусловие: список должен быть непустой
    # постусловие: курсор сместился к началу списка
    def head(self):
        if self.__list_status == LinkedList.LIST_NOT_EMPTY:
            self.__cursor = 0

    # предусловие: список должен быть непустой
    # постусловие: курсор сместился в конец списка
    def tail(self):
        if self.__list_status == LinkedList.LIST_NOT_EMPTY:
            self.__cursor = size() - 1

    # предусловие: справа должен быть хотя бы один элемент
    # постусловие: курсор сместится к элементу справа
    def right(self):
        if self.__list_status == LinkedList.LIST_NOT_EMPTY and self.__cursor < self.size() - 1:
            self.__cursor += 1

    # почему-то отсутствовал вариант с движением в обратную сторону
    # предусловие: слева должен быть хотя бы один элемент
    # постусловие: курсор сместится к элементу слева
    def left(self):
        if self.__list_status == LinkedList.LIST_NOT_EMPTY and self.__cursor > 0:
            self.__cursor -= 1

    # предусловие: требуется рассмотреть несколько граничных условий:
    #  - пустой список
    #  - элемент крайний справа
    #  - элемент не последний
    # постусловие: добавление элемента в конец списка или создание нового списка и замена им старого
    def put_right(self, value):
        if self.__list_status == LinkedList.LIST_EMPTY or self.__cursor == self.size() - 1:
            self.__list.append(value)
        else:
            new_list = self.__list[:self.__cursor+1]
            new_list.append(value)
            new_list.extend(self.__list[self.__cursor+1])
            self.__list = new_list
        self.__list_status = LinkedList.LIST_NOT_EMPTY  # если добавляли в пустой список

    # предусловие: требуется рассмотреть несколько граничных условий:
    #  - пустой список
    #  - элемент крайний слева
    #  - элемент не первый
    # постусловие: добавление элемента в список или создание нового списка и замена им старого
    def put_left(self, value):
        if self.size() == 0:
            self.__list.append(value)
        elif self.__cursor == 0:
            self.__list = [value].extend(self.__list)
        else:
            new_list = self.__list[:self.__cursor]
            new_list.append(value)
            new_list.extend(self.__list[self.__cursor])
            self.__list = new_list
        self.__list_status = LinkedList.LIST_NOT_EMPTY  # если добавляли в пустой список

    # предусловие: требуется рассмотреть несколько граничных условий:
    #  - непустой список и элемент крайний справа (элемент удаляется, курсор уходит на 1 влево)
    #  - просто непустой список (элемент удаляется, курсор остаётся неизменен)
    # постусловие: удаление элемента из списка
    def remove(self):
        if self.size() in (0, 1):  # пустой список или список из одного элемента, операция очищает список
            self.clear()
        else:
            self.__list.pop(self.__cursor)  # удаляет элемент, на который указывает курсор, происходит уменьшение списка на 1

            if self.__cursor == self.size():  # если элемент был крайний справа, курсор уменьшится на 1
                self.__cursor -= 1

    # постусловие: список пуст, курсор не определён
    def clear(self):
        self.__init__()

    # постусловие: список увеличился на единицу
    def add_tail(self, value):
        self.__list.append(value)

    # предусловие: список должен быть непустой
    # постусловие: значение узла списка изменилось
    def replace(self, value):
        if self.__list_status == LinkedList.LIST_NOT_EMPTY:
            self.__list[self.__cursor] = value

    # предусловие: список должен быть непустой
    def remove_all(self, value):
        if self.__list_status == LinkedList.LIST_NOT_EMPTY:
            self.__cursor = 0
            self.__find_status = LinkedList.FIND_NIL
            self.__cursor = self.find(value)
            while self.__find_status != LinkedList.FIND_ERR or self.__list_status == LinkedList.LIST_NOT_EMPTY:
                self.remove()
                self.__cursor = self.find(value)
