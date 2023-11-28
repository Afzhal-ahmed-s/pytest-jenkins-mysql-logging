# Creating a dictionary (equivalent to a Java Map)
my_dict = {
    "apple": 3,
    "banana": 5,
    "cherry": 7,
    "date": 2
}

# Display the dictionary
print("Dictionary:", my_dict)

# Access a value by key (equivalent to Java Map get)
value = my_dict["cherry"]
print("Value for key 'cherry':", value)

# Add a key-value pair (equivalent to Java Map put)
my_dict["fig"] = 4
print("Dictionary after adding 'fig':", my_dict)

# Update the value for a key (equivalent to Java Map put)
my_dict["banana"] = 6
print("Dictionary after updating 'banana':", my_dict)

# Check if a key exists in the dictionary (equivalent to Java Map containsKey)
contains_apple = "apple" in my_dict
print("Dictionary contains key 'apple':", contains_apple)

# Remove a key-value pair (equivalent to Java Map remove)
removed_value = my_dict.pop("date")
print("Dictionary after removing 'date':", my_dict)
print("Removed value:", removed_value)

# Get a list of keys (equivalent to Java Map keySet)
keys = my_dict.keys()
print("Keys in the dictionary:", list(keys))

# Get a list of values (equivalent to Java Map values)
values = my_dict.values()
print("Values in the dictionary:", list(values))

# Get a list of key-value pairs (equivalent to Java Map entrySet)
items = my_dict.items()
print("Key-Value pairs in the dictionary:", list(items))

# Length of the dictionary (equivalent to Java Map size)
dict_length = len(my_dict)
print("Length of the dictionary:", dict_length)

# Clear the dictionary (equivalent to Java Map clear)
my_dict.clear()
print("Dictionary after clearing:", my_dict)
