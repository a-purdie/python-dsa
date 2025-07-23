import linked_lists as ll

# Write a function that converts binary numbers (represented as linked lists)
# to decimal. For example, the linked list 1 -> 1 -> 1 -> 1 is the binary 
# number 1111, which is 15 in decimal.

################
### Solution ###
################

def binary_to_decimal(linked_list):
    binary = ''
    current_node = linked_list.head
    while current_node is not None:
        # Write the node values to a string
        binary += str(current_node.value)
        current_node = current_node.next
    # Not very readable, but this next bit reverses the string, I promise
    # It's because slicing is [start:stop:step], and since start and stop are 
    # omitted, start is just 0 and stop is just len(binary). step = -1 means 
    # stepping backwards one step at a time, so the resulting string is 
    # the reverse
    binary = binary[::-1]
    result = 0 # Initialize the result we'll return
    for i in range(len(binary)):
        # Since the binary string is reversed, we just add 2^i to the result 
        # when the binary digit is 1 and we add nothing otherwise.
        result += (int(binary[i]) * (2 ** i))
    return result

###############################
### Testing for Correctness ###
###############################

### Setup ###

linked_list1 = ll.LinkedList(1)
# Remember, the binary number we are testing has an additional 1 in front
to_append = '10110110110'
for j in to_append:
    linked_list1.append(int(j))

linked_list2 = ll.LinkedList(1)
# Remember, the binary number we are testing has an additional 1 in front
to_append = '101001010101011010010101001'
for k in to_append:
    linked_list2.append(int(k))

### Tests ###

result1 = binary_to_decimal(linked_list1)
assert result1 == 3510

result2 = binary_to_decimal(linked_list2)
assert result2 == 220902569


    