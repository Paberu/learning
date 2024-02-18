class LinkedList:

    def __init__(self):
        self.__list = []
        self.__cursor = None  # указывает на индекс текущего элемента в списке

    def size(self):
        return len(self.__list)

    # предусловие: список должен быть непустой
    # постусловие: курсор сместился к началу списка
    def head(self):
        if size():
            self.__cursor = 0

    # предусловие: список должен быть непустой
    # постусловие: курсор сместился в конец списка
    def tail(self):
        if size():
            self.__cursor = size() - 1

    # предусловие: справа должен быть хотя бы один элемент
    # постусловие: курсор сместится к элементу справа
    def right(self):
        if size > 0 and self.__cursor < size() - 1:
            self.__cursor += 1

    # почему-то отсутствовал вариант с движением в обратную сторону
    # предусловие: слева должен быть хотя бы один элемент
    # постусловие: курсор сместится к элементу слева
    def left(self):
        if size > 0 and self.__cursor > 0:
            self.__cursor -= 1

    # предусловие: список должен быть непустой
    # постусловие: возврат текущего значения
    def get(self):
        if size() > 0:
            return self.__list[self.__cursor]

    # предусловие: требуется рассмотреть несколько граничных условий:
    #  - пустой список
    #  - элемент крайний справа
    #  - элемент не последний
    # постусловие: добавление элемента в конец списка или создание нового списка и замена им старого
    def put_right(self, value):
        if self.size() == 0 or self.size() == cursor + 1:
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
