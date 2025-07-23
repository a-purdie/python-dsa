import linked_lists as ll

# Write a function that removes duplicate valued nodes from the list. 
# The node that occurs first should be the one that remains after duplicates
# are removed.

def remove_duplicates(linked_list):
    # I don't think this is Scott's approach, but I just did it this way and 
    # everything works without using nested loops
    unique_values = [] # We'll keep track of the unique values in the list... 
    # And the indices that contain duplicate values beyond the first occurrence
    # of the value...
    duplicate_indices = []
    current = linked_list.head # Start at the beginning...
    index = 0 # Keep track of which index we're at...
    while current is not None:
        # Iterate through the nodes, each time checking whether we've seen the 
        # node's value before in a prior node
        if current.value not in unique_values:
            # If we haven't, put the value in unique_vlues
            unique_values.append(current.value)
        elif current.value in unique_values:
            # If we have, put the index of the duplicate in duplicate_indices
            duplicate_indices.append(index)
        current = current.next # Move on to the next node
        index += 1 # Increment the index and do it again until current is None
    # Reverse the list of duplicate indices so that as we remove duplicates, 
    # the indices of the remaining duplicates don't decrement by one each time
    duplicate_indices.reverse()
    for index in duplicate_indices: # Remove the duplicates
        to_remove = linked_list.get(index) # Keep track of the duplicate... 
        previous = linked_list.get(index - 1) # And the node pointing to it...
        # Set the previous node to the duplicate's next node...
        previous.next = to_remove.next
        # Set the duplicate's next attribute to None to finish removing it 
        # from the list...
        to_remove.next = None
        # And don't forget to decrement the list's length
        linked_list.length -= 1
        # Repeat until all the duplicates are gone
    return linked_list

###############################
### Testing for Correctness ###
###############################

### Setup ###

# This list looks like 1 1 2 2 3 3 4 4 5 5
linked_list1 = ll.LinkedList(1) 
linked_list1.append(1)
for i in range(4):
    linked_list1.append(i + 2)
    linked_list1.append(i + 2)

# This list looks like 1 2 3 4 5 ... 998 999 1000; no dups
linked_list2 = ll.LinkedList(1) # A long, even cardinality linked list
for i in range(999):
    linked_list2.append(i + 2)

### Tests ###

result1 = remove_duplicates(linked_list1)
result2 = remove_duplicates(linked_list2)

assert result1.length == 5
# After removing duplicates from linked_list1, it should be 1 2 3 4 5
# Check every node to make sure it's the right value
current_value = 1
current_node = result1.head
while current_node is not None:
    assert current_node.value == current_value
    current_value += 1
    current_node = current_node.next

assert result2.length == 1000
# No duplicates to remove from linked_list2, so it should be the same list
# Again, check every node to make sure it's the right value
current_value = 1
current_node = result2.head
while current_node is not None:
    assert current_node.value == current_value
    current_value += 1
    current_node = current_node.next