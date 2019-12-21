from doubly_linked_list import DoublyLinkedList


class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.current = None
        self.storage = DoublyLinkedList()

    def append(self, item):
        if self.storage.length != self.capacity:
            self.current = self.storage.head  # olest
            self.storage.add_to_tail(item)  # add
        else:
            # at capacity, replace head with item
            self.current.value = item
            # set the current node to next node, unless current is at tail, then reset to head
            if self.current is self.storage.tail:
                self.current = self.storage.head
            else:
                self.current = self.current.next

    def get(self):
        # Note:  This is the only [] allowed
        list_buffer_contents = []
        # TODO: Your code here
        node = self.storage.head
        while node:
            list_buffer_contents.append(node.value)
            node = node.next
        return list_buffer_contents


# buffer = RingBuffer(3)
# buffer.append("a")
# buffer.append("b")
# buffer.append("c")
# buffer.append("d")
# buffer.append("e")
# buffer.get()
# buffer.append("f")


# ----------------Stretch Goal-------------------


class ArrayRingBuffer:
    def __init__(self, capacity):
        pass

    def append(self, item):
        pass

    def get(self):
        pass
