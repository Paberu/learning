from ParentQueue import ParentQueue


class Queue(ParentQueue):

    def __init__(self):
        super().__init__()

    def enqueue(self, value):
        super()._add_tail(value)

    def dequeue(self):
        return super()._pop_head()

    def peek(self):
        return super()._peek_head()
