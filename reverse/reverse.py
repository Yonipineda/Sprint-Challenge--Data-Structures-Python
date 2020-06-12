class Node:
    def __init__(self, value=None, next_node=None):
        self.value = value
        self.next_node = next_node

    def get_value(self):
        return self.value

    def get_next(self):
        return self.next_node

    def set_next(self, new_next):
        self.next_node = new_next
        return new_next

class LinkedList:
    def __init__(self):
        self.head = None

    def add_to_head(self, value):
        node = Node(value)

        if self.head is not None:
            node.set_next(self.head)

        self.head = node

    def contains(self, value):
        if not self.head:
            return False

        current = self.head

        while current:
            if current.get_value() == value:
                return True

            current = current.get_next()

        return False

    def reverse_list(self, node, prev):
        if node == None: # checks for empty cases and returns None if so 
            return None 
        elif node.get_next() == None: # checks for single values and last link 
            self.head = node # node to new head 
            return node # return the new node 
        # checks for middle of a multi-link lisr 
        next_node = node.get_next()
        r = self.reverse_list(next_node, None)
        r = r.set_next(node)
        return r
