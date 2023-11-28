# Creating a set (equivalent to a Java Set)
my_set = {1, 2, 3, 4, 5}

# Display the set
print("Set:", my_set)

# Add elements to the set (equivalent to Java Set add)
my_set.add(6)
my_set.add(7)
print("Set after adding 6 and 7:", my_set)

# Remove an element from the set (equivalent to Java Set remove)
my_set.remove(3)
print("Set after removing 3:", my_set)

# Check if an element is in the set (equivalent to Java Set contains)
contains_4 = 4 in my_set
print("Set contains 4:", contains_4)

# Length of the set (equivalent to Java Set size)
set_length = len(my_set)
print("Length of the set:", set_length)

# Create another set (equivalent to Java Set)
other_set = {3, 4, 5}

# Union of two sets (equivalent to Java Set union)
union_set = my_set.union(other_set)
print("Union of two sets:", union_set)

# Intersection of two sets (equivalent to Java Set retainAll)
intersection_set = my_set.intersection(other_set)
print("Intersection of two sets:", intersection_set)

# Difference between two sets (equivalent to Java Set removeAll)
difference_set = my_set.difference(other_set)
print("Difference between two sets:", difference_set)

# Check if one set is a subset of another (equivalent to Java Set containsAll)
is_subset = other_set.issubset(my_set)
print("Is other_set a subset of my_set?", is_subset)

# Clear the set (equivalent to Java Set clear)
my_set.clear()
print("Set after clearing:", my_set)

print(sorted(my_set))
