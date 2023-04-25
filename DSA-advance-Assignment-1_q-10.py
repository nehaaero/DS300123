class QueueUsingStack:
    def __init__(self):
        """
        Initialize an empty queue using two stacks.
        """
        self.stack1 = []
        self.stack2 = []

    def is_empty(self):
        """
        Check if the queue is empty.
        Returns:
            bool: True if the queue is empty, False otherwise.
        """
        return len(self.stack1) == 0 and len(self.stack2) == 0

    def size(self):
        """
        Get the current size of the queue.
        Returns:
            int: The size of the queue.
        """
        return len(self.stack1) + len(self.stack2)

    def enqueue(self, item):
        """
        Add an item to the end of the queue.
        Args:
            item: The item to be enqueued.
        """
        self.stack1.append(item)

    def dequeue(self):
        """
        Remove and return the item from the front of the queue.
        Returns:
            item: The item that was dequeued.
        """
        if len(self.stack2) == 0:
            while len(self.stack1) > 0:
                self.stack2.append(self.stack1.pop())

        if len(self.stack2) == 0:
            return None

        return self.stack2.pop()

queue = QueueUsingStack()
queue.enqueue(1)
queue.enqueue(2)
queue.enqueue(3)
print("Queue size:", queue.size())  
print("Dequeued item:", queue.dequeue())  
print("Dequeued item:", queue.dequeue())  
print("Queue size:", queue.size()) 