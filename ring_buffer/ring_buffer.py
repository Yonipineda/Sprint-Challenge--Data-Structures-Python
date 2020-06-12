from doubly_linked_list import DoublyLinkedList

class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity 
        self.current = None 
        self.storage = DoublyLinkedList()

    def append(self, item):
        if self.storage.length < self.capacity:
            self.storage.add_to_tail(item) # Adds new item to head 
            self.current = self.storage.head # places current at head 
        else: 
            if self.current == self.storage.head:
                self.storage.remove_from_head()
                self.storage.add_to_head(item)
                self.current = self.storage.head.next # current to second item 
            elif self.current == self.storage.tail: # @ tail 
                self.storage.remove_from_tail()
                self.storage.add_to_tail(item)
                self.current = self.storage.head
            else:
                self.current = self.current.next 
                self.current.insert_before(item) # add item before current 
                self.current.prev.prev.delete() # delete the oldest element 

    def get(self):
        buffer_content = []
        if self.storage.length > 0:
            current = self.storage.head 
            buffer_content.append(current.value)
            while current.next:
                current = current.next
                buffer_content.append(current.value)
            return buffer_content