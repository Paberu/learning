class LinkedList:

    LIST_EMPTY: Final = 0
    LIST_NOT_EMPTY: Final = 1
    CURSOR_NIL: Final = 0
    CURSOR_OK: Final = 1
    CURSOR_ERR: Final = 2

    def __init__(self):
        self.__list = []
        self.__cursor = None  # указывает на индекс текущего элемента в списке

        self.__list_status = LinkedList.LIST_EMPTY
        self.__cursor_status = LinkedList.CURSOR_NIL

    # запрос
    def size(self):
        return len(self.__list)

    # предусловие: список должен быть непустой
    # постусловие: возврат текущего значения
    def get(self):
        if LinkedList.LIST_NOT_EMPTY:
            return self.__list[self.__cursor]

    # команды

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
        if self.__list_status == LinkedList.LIST_NOT_EMPTY and self.__cursor < size() - 1:
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
        if self.__list_status == LinkedList.LIST_NOT_EMPTY or self.size() == cursor + 1:
            self.__list.append(value)
        else:
            new_list = self.__list[:self.__cursor+1]
            new_list.append(value)
            new_list.extend(self.__list[self.__cursor+1])
            self.__list = new_list

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

    # предусловие: требуется рассмотреть несколько граничных условий:
    #  - непустой список и элемент крайний справа (элемент удаляется, курсор уходит на 1 влево)
    #  - просто непустой список (элемент удаляется, курсор остаётся неизменен)
    # постусловие: удаление элемента из списка
    def remove(self):
        if self.size() != 0:
            self.__list.pop(self.__cursor)  # удаляет элемент, на который указывает курсор, происходит уменьшение списка на 1
        if self.__cursor == self.size():  # если элемент был крайний справа, курсор уменьшится на 1
            self.__cursor -= 1

    # постусловие: список пуст, курсор не определён
    def clear(self):
        self.__init__(self)

    def add_tail(self, value):
        self.__list.append(value)

    def replace(self, value):
        self.__list[self.__cursor] = value

    def find(self, value):
        try:
            self.__cursor = self.__list.index(value, self.__cursor)
        except ValueError:
            pass

    def remove_all(self, value):
        self.

    def is_head(self):
        if self.size() > 0:
            return self.__cursor == 0

    def is_tail(self):
        if self.size() > 0:
            return self.__cursor == self.size() - 1

    def is_value(self):
        if self.size() > 0:
            return True