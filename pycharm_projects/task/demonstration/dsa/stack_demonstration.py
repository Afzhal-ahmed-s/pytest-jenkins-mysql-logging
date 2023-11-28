# Create an empty stack
stack = []

# Push elements onto the stack (equivalent to Java Stack push)
stack.append(1)
stack.append(2)
stack.append(3)

# Display the stack (top of the stack is the end of the list)
print("Stack:", stack)

# Pop elements from the stack (equivalent to Java Stack pop)
popped_element = stack.pop()
print("Popped element:", popped_element)
print("Stack after popping:", stack)

# Check if the stack is empty
is_empty = len(stack) == 0
print("Is the stack empty?", is_empty)

# Get the top element without removing it (equivalent to Java Stack peek)
top_element = stack[-1]
print("Top element:", top_element)

# Get the size of the stack
stack_size = len(stack)
print("Size of the stack:", stack_size)

# Clear the stack (remove all elements)
stack.clear()
print("Stack after clearing:", stack)
