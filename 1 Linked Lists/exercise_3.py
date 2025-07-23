import linked_lists as ll

# Write a function that finds the k-th node from the end of the linked list, 
# where the tail corresponds to k = 1. If k > length of the linked list, 
# return None.

################
### Solution ###
################

def kth_node_from_end(linked_list, k):
    fast = linked_list.head
    slow = linked_list.head
    # First, advance fast k nodes ahead
    # If fast ends up being None during this loop, then k > length of the 
    # linked list and we return None
    for _ in range(k):
        if fast is None:
            return None
        fast = fast.next
    # Once fast is advanced k nodes, advance both fast and slow one node at a 
    # time until fast reaches the end of the list, which will put slow exactly 
    # at the kth node from the end of the linked list
    while fast is not None:
        fast = fast.next
        slow = slow.next
    return slow

###############################
### Testing for Correctness ###
###############################

### Setup ###

linked_list1 = ll.LinkedList(1) # A short, odd cardinality linked list
for i in range(4):
    linked_list1.append(i + 2)

linked_list2 = ll.LinkedList(1) # A linked list with a single element

linked_list3 = ll.LinkedList(1) # An empty linked list
linked_list3.pop()

linked_list4 = ll.LinkedList(1) # A long, even cardinality linked list
for i in range(999):
    linked_list4.append(i + 2)

### Tests ###

result1 = kth_node_from_end(linked_list1, 2) # Return node with value 4
result2 = kth_node_from_end(linked_list2, 1) # Return node with value 1
result3 = kth_node_from_end(linked_list3, 3) # Return None
result4 = kth_node_from_end(linked_list4, 600) # Return node with value 401

print(
    f"Result 1: {result1.value} | Result 2: {result2.value} | "
    f"Result 3: {result3} | Result 4: {result4.value}"
)

assert 4 == result1.value
assert 1 == result2.value
assert None == result3
assert 401 == result4.value