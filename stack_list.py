class Stack:
    def __init__(self, d, n=None):
        self.node = n
        self.data = d

    def get_prev(self):
        return self.node

    def set_prev(self, n):
        self.node = n

    def get_data(self):
        return self.data

    def set_data(self, d):
        self.data = d


class ShankarStack:
    def __init__(self):
        self.empty = True
        self.size = 0
        self.peek = None

    def push(self, node):
        new_node = Stack(node, self.peek)
        self.peek = new_node
        self.size += 1
        self.empty = False

    def pop(self):
        self.peek = self.peek.get_prev()
        self.size -= 1

    def size(self):
        return self.size

    def checking(self, user_input):
        peeking = self.peek
        for every_num in range(self.size):
            if peeking.get_data() == user_input:
                return True
            peeking = peeking.get_prev()
        return False

    def empty(self):
        return self.empty






