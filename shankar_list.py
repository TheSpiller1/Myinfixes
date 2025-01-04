class Node:
    def __init__(self, d, n=None):
        self.prev_node = n
        self.data = d

    def get_prev(self):
        return self.prev_node

    def set_prev(self, n):
        self.prev_node = n

    def get_data(self):
        return self.data

    def set_data(self, d):
        self.data = d


class ShankarLinkedLists:
    def __init__(self):
        self.root = None
        self.size = 0
        self.linked_list = []

    def print_list(self, c, result, prin=True, num=0):

        if c == 1:
            self.linked_list.append(result)
            if prin:
                print(f"""User just added {result} to the linked list.
Current Linked list: {self.linked_list}
""")
        elif c == 2:
            self.linked_list.remove(result)
            if prin:
                print(f"""User just deleted {result} from the linked list.
Current Linked list: {self.linked_list}
""")

        else:
            self.linked_list.insert(self.size - num, result)
            print(f"""User just rotated {result},  {num} places in the linked list.
            Current Linked list: {self.linked_list}""")
            
    def size(self):
        return self.size

    def add(self, d, prin):
        new_node = Node(d, self.root)
        self.root = new_node
        self.size += 1
        if prin:
            ShankarLinkedLists.print_list(self, 1, d, True)
        else:
            ShankarLinkedLists.print_list(self, 1, d, False)

    def find(self, d):
        node = self.root
        counter = 0
        while node:

            if node.get_data() == d:
                return counter
            else:
                node = node.get_prev()
                counter += 1

        return False

    def delete(self, d, prin):
        current_node = self.root
        next_node = None
        count = 0
        while current_node:
            if current_node.get_data() == d:
                if next_node:
                    next_node.set_prev(current_node.get_prev())
                    next_node.set_data(next_node.get_data())

                else:
                    self.root = current_node.get_prev()
                self.size -= 1
                break
            else:
                next_node = current_node
                current_node = current_node.get_prev()
                count += 1

        if prin:
            ShankarLinkedLists.print_list(self, 2, d, True)

        else:
            ShankarLinkedLists.print_list(self, 2, d, False)

    def access_list(self):
        return self.linked_list

