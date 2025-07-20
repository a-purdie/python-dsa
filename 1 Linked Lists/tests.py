from linked_lists import LinkedList, Node

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