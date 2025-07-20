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

print("Before Pop:")
my_linked_list = LinkedList(4)
my_linked_list.append(3)
my_linked_list.append(5)
my_linked_list.print_list()


print(f"Value of get node 1: {my_linked_list.get(1).value}")
my_linked_list.set_value(1, 100)
print(f"Value of node 1 after set to 100: {my_linked_list.get(1).value}")

my_linked_list.insert(1, 250)
print(f"List after inserting 250 at index 1")
my_linked_list.print_list()
print(f"Current length: {my_linked_list.length}")

my_linked_list.insert(0, 300)
print(f"List after inserting 300 at index 0")
my_linked_list.print_list()
print(f"Current length: {my_linked_list.length}")

my_linked_list.reverse()
print(f"After reverse:")
my_linked_list.print_list()


my_linked_list.insert(5, 400)
print(f"List after inserting 400 at index 5")
my_linked_list.print_list()
print(f"Current length: {my_linked_list.length}")

my_linked_list.insert(100, 500)
print(f"List after trying to insert 500 at index 100")
my_linked_list.print_list()
print(f"Current length: {my_linked_list.length}")

my_linked_list.remove(1)
print(f"List after removing index 1:")
my_linked_list.print_list()
print(f"Current length: {my_linked_list.length}")

my_linked_list.remove(0)
print(f"List after removing index 0:")
my_linked_list.print_list()
print(f"Current length: {my_linked_list.length}")

my_linked_list.remove(my_linked_list.length - 1)
print(f"List after removing index length - 1:")
my_linked_list.print_list()
print(f"Current length: {my_linked_list.length}")

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
