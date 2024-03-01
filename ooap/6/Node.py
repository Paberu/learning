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
        if node:
            node._previous = self

    def set_previous(self, node):
        self._previous = node
        if node:
            node._next = self

    def get_value(self):
        return self._value
