# Linked list implementation from scratch

class Node:
    def __init__(self, value):
        self.value = value
        self.next: Node | None = None

class LinkedList:
    def __init__(self, value):
        new_node = Node(value)
        self.head: Node | None = new_node
        self.tail: Node | None = new_node
        self.length = 1

    def print_list(self):
        temp = self.head
        while temp is not None:
            print(temp.value)
            temp = temp.next

    def append(self, value):
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1
        return True
    
    def pop(self):
        if self.length == 0:
            return None
        current = self.head
        next = current.next
        if self.length == 1:
            self.head = None
            self.tail = None
            self.length = 0
            return current
        while next is not None:
            previous = current
            current = next
            next = next.next
        self.tail = previous
        self.tail.next = None
        self.length -= 1
        return current
    
    def prepend(self, value):
        new_node = Node(value)
        new_node.next = self.head
        self.head = new_node
        self.length += 1
        if self.length == 1:
            self.tail = new_node
        return True

    def pop_first(self):
        if self.length == 0:
            return None
        old_head = self.head
        new_head = self.head.next
        self.head.next = None
        self.head = new_head
        self.length -= 1
        if self.length == 0:
            self.tail = None
        return old_head
    
    def get(self, index: int):
        if index < 0 or index > self.length - 1:
            return None
        current_node = self.head
        for _ in range(index):
            current_node = current_node.next
        return current_node
    
    def set_value(self, index: int, value):
        current_node = self.get(index)
        if current_node is not None:
            current_node.value = value
            return True
        else:
            return False
        
    def insert(self, index: int, value):
        if index < 0 or index > self.length:
            return False
        elif index == 0:
            self.prepend(value)
        elif index == self.length:
            self.append(value)
        else:
            new_node = Node(value)
            current = self.head
            previous = None
            for _ in range(index):
                previous = current
                current = current.next
            previous.next = new_node
            new_node.next = current
            self.length += 1
        return True
    
    def remove(self, index: int):
        if index < 0 or index >= self.length:
            return None
        if index == 0:
            return self.pop_first()
        elif index == self.length - 1:
            return self.pop()
        else:
            previous = self.get(index - 1)
            current = previous.next
            previous.next = current.next
            current.next = None
            self.length -= 1
            return current

    def reverse(self):
        if self.length <= 1:
            return True
        previous = None
        current = self.head
        next = current.next
        self.tail = current
        while current is not None:
            next = current.next
            current.next = previous
            previous = current
            current = next
        self.head = previous
        return True