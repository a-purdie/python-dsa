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

print("Before Pop:")
my_linked_list = LinkedList(4)
my_linked_list.append(3)
my_linked_list.append(5)
my_linked_list.print_list()


print(f"Value of get node 1: {my_linked_list.get(1).value}")

print("After Prepend")
my_linked_list.prepend(20)
my_linked_list.print_list()
print(f"Not empty list head: {my_linked_list.head.value}")
print(f"Not empty list tail: {my_linked_list.tail.value}")

print("After pop first")
my_linked_list.pop_first()
my_linked_list.print_list()
print(f"Not empty list head: {my_linked_list.head.value}")
print(f"Not empty list tail: {my_linked_list.tail.value}")

empty_list = LinkedList(4)
empty_list.pop()

print("Prepending an empty list")
empty_list.prepend(20)
empty_list.print_list()
print(f"Empty list head: {empty_list.head.value}")
print(f"Empty list tail: {empty_list.tail.value}")

print("After pop first")
empty_list.pop_first()
empty_list.print_list()
print(f"Not empty list head: {empty_list.head}")
print(f"Not empty list tail: {empty_list.tail}")
