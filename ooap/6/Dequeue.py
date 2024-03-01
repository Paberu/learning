from ParentQueue import ParentQueue


class Dequeue(ParentQueue):

    def __init__(self):
        super().__init__()

    def add_tail(self, value):
        super()._add_tail(value)

    def add_head(self, value):
        super()._add_head(value)

    def pop_head(self):
        return super()._pop_head()

    def pop_tail(self):
        return super()._pop_tail()

    def peek_head(self):
        return super()._peek_head()

    def peek_tail(self):
        return super()._peek_tail()