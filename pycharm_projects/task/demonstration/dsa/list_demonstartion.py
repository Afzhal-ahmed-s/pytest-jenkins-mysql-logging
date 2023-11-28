# Create a list
my_list = [1, 2, 3, 4, 5]

# Display the list
print("List:", my_list)

# Get the length of the list
list_length = len(my_list)
print("Length of the list:", list_length)

# Access elements by index
element = my_list[2]
print("Element at index 2:", element)

# Check if an element is in the list
contains_3 = 3 in my_list
print("List contains 3:", contains_3)

# Find the index of an element
index_of_4 = my_list.index(4)
print("Index of 4:", index_of_4)

# Add an element to the end of the list
my_list.append(6)
print("List after appending 6:", my_list)

# Insert an element at a specific index
my_list.insert(1, 7)
print("List after inserting 7 at index 1:", my_list)

# Remove the first occurrence of an element
my_list.remove(3)
print("List after removing the first occurrence of 3:", my_list)

# Remove an element by index
removed_element = my_list.pop(2)
print("List after removing the element at index 2:", my_list)
print("Removed element:", removed_element)

# Check if the list is empty
is_empty = len(my_list) == 0
print("Is the list empty?", is_empty)

# Reverse the list
my_list.reverse()
print("List after reversing:", my_list)

# Sort the list in ascending order
my_list.sort()
print("List after sorting in ascending order:", my_list)

# Sort the list in descending order
my_list.sort(reverse=True)
print("List in Descending Order:", my_list)
