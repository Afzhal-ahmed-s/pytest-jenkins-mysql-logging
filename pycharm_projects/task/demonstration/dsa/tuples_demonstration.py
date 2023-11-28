# Creating a tuple (equivalent to an immutable Java List)
my_tuple = (1, 2, 3, 4, 5)

# Access elements by index (equivalent to Java List or ArrayList)
element = my_tuple[2]
print("Element at index 2:", element)

# Check if an element is in the tuple (equivalent to Java List or ArrayList contains)
contains_3 = 3 in my_tuple
print("Tuple contains 3:", contains_3)

# Find the index of an element (equivalent to Java List or ArrayList indexOf)
index_of_4 = my_tuple.index(4)
print("Index of 4:", index_of_4)

# Count the occurrences of an element (equivalent to Java List or ArrayList count)
count_of_5 = my_tuple.count(5)
print("Count of 5:", count_of_5)

# Slicing a tuple (equivalent to Java List or ArrayList subList)
subset = my_tuple[1:4]
print("Subset:", subset)

# Concatenate tuples (equivalent to Java ArrayList.addAll)
other_tuple = (6, 7, 8)
concatenated_tuple = my_tuple + other_tuple
print("Concatenated Tuple:", concatenated_tuple)

# Unpacking a tuple into variables (equivalent to Java variable assignment)
a, b, c, d, e = my_tuple
print("Unpacked Variables:", a, b, c, d, e)

# Length of the tuple (equivalent to Java List or ArrayList size)
tuple_length = len(my_tuple)
print("Length of the tuple:", tuple_length)
