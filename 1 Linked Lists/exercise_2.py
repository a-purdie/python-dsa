import linked_lists as ll

# Write a function that checks whether a linked list contains a loop

################
### Solution ###
################

def has_loop(linked_list):
    # The approach will be to have two temporary variables that iterate 
    # through the list. Similar to the middle node function in exercise_1, 
    # one of the variables will move to the next node at each iteration, and 
    # the other will move to the next node every other iteration. There is 
    # no loop if the "faster" variable reaches the end of the list, i.e., 
    # fast == None. There is a loop if, at any point after the first advance 
    # of the "faster" variable, the two variables are equal to each other.
    slow = linked_list.head
    fast = linked_list.head

    # We'll flip this flag to its opposite value each iteration. It needs to 
    # be initialized as False because otherwise, fast == slow at the start of 
    # the second iteration no matter what, so every linked list would be 
    # labeled as having a loop even though it wouldn't be true.
    advance_slow = False
    while True: # Run the loop until a terminating condition is met
        fast = fast.next # Advance the fast variable
        if fast is None:
            return False # If fast is at the end of the list, we're done
        if fast == slow:
            return True # If fast and slow are the same node, we're done
        if advance_slow:
            slow = slow.next # Otherwise advance slow if applicable this iter
        advance_slow = not advance_slow # Flip the advance_slow flag

###############################
### Testing for Correctness ###
###############################

### Setup ###

no_loop = ll.LinkedList(1)
for i in range(4):
    no_loop.append(i)

loop = ll.LinkedList(1)
for i in range(4):
    loop.append(i)
loop.tail.next = loop.head

singleton = ll.LinkedList(1)

### Tests ###

result1 = has_loop(no_loop) # Result should be False
result2 = has_loop(loop) # Result should be True
result3 = has_loop(singleton) # Result should be False

print(f"Result 1: {result1} | Result 2: {result2} | Result 3: {result3}")

assert result1 == False
assert result2 == True
assert result3 == False