import linked_lists as ll

# Return the middle node of the linked list without using the 
# length attribute and only interating over the list once

################
### Solution ###
################

def find_middle_node(linked_list: ll.LinkedList):
    if linked_list.head == linked_list.tail:
    # If the list is empty or has only one element...
        return linked_list.head
        # Then just return the head.

    # As we iterate through the linked list, we'll keep track of which node 
    # is the middle node so far with middle_node
    middle_node = linked_list.head

    # Keep track of where we are in the linked list with current
    current = linked_list.head

    # Use after to check for when we've reached the end of the linked list
    after = current.next

    # To maintain the middle node, we will want to "advance" the middle node 
    # forward one node in the chain every other iteration, so we'll flip 
    # advance_middle_node to its opposite each iteration. Whether this flag 
    # starts as True or False doesn't change the result when the length of the
    # linked list is an odd number, but it will change the result when it's 
    # even. When set to True, the result will return the first node of the 
    # second half of the linked list. When set to False, it will return the 
    # final node of the first half.
    advance_middle_node = True

    # We only want to continue until after is not None since that indicates 
    # that we've reached the final node in the list
    while after is not None:
        current = after # Advance the current node to the next one in the list
        after = after.next # Advance after to the next node in the list
        if advance_middle_node: # Check whether we move the middle node this iteration
            middle_node = middle_node.next
        # Flip the advance_middle_node indicator for next time
        advance_middle_node = not advance_middle_node
    return middle_node

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

result1 = find_middle_node(linked_list1) # value should be 3
result2 = find_middle_node(linked_list2) # value should be 1
result3 = find_middle_node(linked_list3) # should be None
result4 = find_middle_node(linked_list4) # should be 501
print(
    f"Result 1: {result1.value} | Result 2: {result2.value} | "
    f"Result 3: {result3} | Result 4: {result4.value}"
)

assert 3 == result1.value
assert 1 == result2.value
assert None == result3
assert 501 == result4.value