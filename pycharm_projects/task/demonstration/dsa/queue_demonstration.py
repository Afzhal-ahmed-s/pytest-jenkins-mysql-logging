import queue

# Create a queue
my_queue = queue.Queue()

# Enqueue elements (equivalent to Java Queue offer/enqueue)
my_queue.put(1)
my_queue.put(2)
my_queue.put(3)

# Display the queue
print("Queue:", list(my_queue.queue))

# Dequeue elements (equivalent to Java Queue poll/dequeue)
dequeued_element = my_queue.get()
print("Dequeued element:", dequeued_element)
print("Queue after dequeue:", list(my_queue.queue))

# Check if the queue is empty (equivalent to Java Queue isEmpty)
is_empty = my_queue.empty()
print("Is the queue empty?", is_empty)

# Get the size of the queue (equivalent to Java Queue size)
queue_size = my_queue.qsize()
print("Size of the queue:", queue_size)

# Clear the queue (remove all elements)
while not my_queue.empty:
    my_queue.get()
print("Queue after clearing:", list(my_queue.queue))
